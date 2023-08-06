#  Copyright 2019-2020 The Solas Authors.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import solas
from solas.interestingness.interestingness import interestingness
from solas.vis.Vis import Vis
from solas.vis.VisList import VisList
from solas.processor.Compiler import Compiler
from solas.utils import utils
from solas.utils.utils import get_filter_specs

from IPython.core.debugger import set_trace


def add_filter(ldf, **kwargs):
    """
    Iterates over all possible values of a categorical variable and generates visualizations where each categorical value filters the data.

    Parameters
    ----------
    ldf : solas.core.frame
            SolasDataFrame with underspecified intent.

    Returns
    -------
    recommendations : Dict[str,obj]
            object with a collection of visualizations that result from the Filter action.
    """
    filters = utils.get_filter_specs(ldf._intent)
    filter_values = []
    output = []

    # if fltr is specified, create visualizations where data is filtered by all values of the fltr's categorical variable
    column_spec = utils.get_attrs_specs(ldf._intent)
    column_spec_attr = list(map(lambda x: x.attribute, column_spec))
    recommendation = {
        "action": "",
        "description": "",
        "long_description": "",
    }
    if len(filters) == 1:
        # get unique values for all categorical values specified and creates corresponding filters
        fltr = filters[0]

        if ldf.data_type[fltr.attribute] == "nominal":
            recommendation = {
                "action": "Filter",
                "description": f"Changing the <p class='highlight-intent'>{fltr.attribute}</p> filter to an alternative value.",
                "long_description": f"Swap out the filter value for {fltr.attribute} to other possible values, while keeping all else the same. Visualizations are ranked based on interestingness",
            }
            unique_values = ldf.unique_values[fltr.attribute]
            filter_values.append(fltr.value)
            # creates vis with new filters
            for val in unique_values:
                if val not in filter_values:
                    new_spec = column_spec.copy()
                    new_filter = solas.Clause(attribute=fltr.attribute, value=val)
                    new_spec.append(new_filter)
                    temp_vis = Vis(new_spec)
                    output.append(temp_vis)
        elif ldf.data_type[fltr.attribute] == "quantitative":
            recommendation = {
                "action": "Filter",
                "description": f"Changing the <p class='highlight-intent'>{fltr.attribute}</p> filter to an alternative inequality operation.",
                "long_description": f"Changing the <p class='highlight-intent'>{fltr.attribute}</p> filter to an alternative inequality operation.",
            }

            def get_complementary_ops(fltr_op):
                if fltr_op == ">":
                    return "<="
                elif fltr_op == "<":
                    return ">="
                elif fltr_op == ">=":
                    return "<"
                elif fltr_op == "<=":
                    return ">"
                # TODO: need to support case where fltr_op is "=" --> auto-binned ranges

            # Create vis with complementary filter operations
            new_spec = column_spec.copy()
            new_filter = solas.Clause(
                attribute=fltr.attribute,
                filter_op=get_complementary_ops(fltr.filter_op),
                value=fltr.value,
            )
            new_spec.append(new_filter)
            temp_vis = Vis(new_spec, score=1)
            output.append(temp_vis)
    # if no existing filters, create filters using unique values from all categorical variables in the dataset
    else:
        intended_attrs = ", ".join(
            [
                str(clause.attribute)
                for clause in ldf._intent
                if clause.value == "" and clause.attribute != "Record"
            ]
        )
        recommendation = {
            "action": "Filter",
            "description": f"Applying filters to the <p class='highlight-intent'>{intended_attrs}</p> intent.",
            "long_description": f"Adding any filter while keeping the attributes on the x and y axes fixed. Visualizations are ranked based on interestingness",
        }
        categorical_vars = []
        for col in list(ldf.columns):
            # if cardinality is not too high, and attribute is not one of the X,Y (specified) column
            if 1 < ldf.cardinality[col] < 30 and col not in column_spec_attr:
                categorical_vars.append(col)
        for cat in categorical_vars:
            unique_values = ldf.unique_values[cat]
            for val in unique_values:
                new_spec = column_spec.copy()
                new_filter = solas.Clause(attribute=cat, filter_op="=", value=val)
                new_spec.append(new_filter)
                temp_vis = Vis(new_spec)
                output.append(temp_vis)
    if (
        ldf.current_vis is not None
        and len(ldf.current_vis) == 1
        and ldf.current_vis[0].mark == "line"
        and len(get_filter_specs(ldf.intent)) > 0
    ):
        recommendation = {
            "action": "Similarity",
            "description": "Show other charts that are visually similar to the Current vis.",
            "long_description": "Show other charts that are visually similar to the Current vis.",
        }
        last = get_filter_specs(ldf.intent)[-1]
        # originally the code is:
        #   output = ldf.intent.copy()[0:-1]
        # but we cannot guarantee that the filter clause is always the last one
        output = [intent for intent in ldf.intent.copy() if not (intent.attribute == last.attribute and hasattr(intent, "value") and (last.value == intent.value))]
        # array of possible values for attribute
        arr = ldf[last.attribute].unique().tolist()
        # remove the one with the exactly same filter as current vis
        arr = [_arr for _arr in arr if _arr != last.value]
        output.append(solas.Clause(last.attribute, last.attribute, arr))
    vlist = solas.vis.VisList.VisList(output, ldf)
    vlist_copy = solas.vis.VisList.VisList(output, ldf)
    for i in range(len(vlist_copy)):
        vlist[i].score = interestingness(vlist_copy[i], ldf)
    col_order = ldf.history.get_implicit_intent(ldf.columns)
    vlist.sort(intent_cols=col_order)
    vlist.filter(**kwargs)
    vlist = vlist.showK()
    recommendation["collection"] = vlist
    return recommendation
