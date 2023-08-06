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

# from ..solasDataFrame.SolasDataframe import SolasDataFrame
from solas.core.frame import SolasDataFrame
from solas.vis.Clause import Clause
from typing import List
from solas.utils.date_utils import is_datetime_series, is_datetime_string
import warnings
import pandas as pd
import solas
import solas.utils.utils


class Validator:
    """
    Contains methods for validating solas.Clause objects in the intent.
    """

    def __init__(self):
        self.name = "Validator"
        warnings.formatwarning = solas.warning_format

    def __repr__(self):
        return f"<Validator>"

    @staticmethod
    def validate_intent(intent: List[Clause], ldf: SolasDataFrame, suppress_warning=False):
        """
        Validates input specifications from the user to find inconsistencies and errors.

        Parameters
        ----------
        ldf : solas.core.frame
                SolasDataFrame with underspecified intent.

        Returns
        -------
        Boolean
                True if the intent passed in is valid, False otherwise.

        Raises
        ------
        ValueError
                Ensures input intent are consistent with DataFrame content.

        """

        def validate_clause(clause, g_mark_type):
            warn_msg = ""

            # check that specified vis types are consistent

            # TODO move this list of valid vis somewhere dynamic
            if clause.mark_type and clause.mark_type not in [
                "histogram",
                "bar",
                "scatter",
                "line",
                "heatmap",
                "boxplot",
            ]:
                warn_msg = "\n -Vis type must be in ['histogram', 'bar', 'scatter', 'line', 'heatmap', 'boxplot']"
            elif not g_mark_type and clause.mark_type:
                g_mark_type = clause.mark_type
            elif g_mark_type and clause.mark_type:
                if g_mark_type != clause.mark_type:
                    warn_msg = f"\n- Intents must all have same vis type specified. {g_mark_type} != {clause.mark_type}"

            if not (clause.attribute == "?" or clause.value == "?" or clause.attribute == ""):
                if isinstance(clause.attribute, list):
                    for attr in clause.attribute:
                        if attr not in list(ldf.columns):
                            warn_msg = (
                                f"\n- The input attribute '{attr}' does not exist in the DataFrame."
                            )
                else:
                    if clause.attribute != "Record":
                        # we don't value check datetime since datetime can take filter values that don't exactly match the exact TimeStamp representation
                        if isinstance(clause.attribute, str) and not is_datetime_string(
                            clause.attribute
                        ):
                            if not clause.attribute in list(ldf.columns):
                                search_val = clause.attribute
                                match_attr = False
                                for attr, val_list in ldf.unique_values.items():
                                    if search_val in val_list:
                                        match_attr = attr
                                if match_attr:
                                    warn_msg = f"\n- The input '{search_val}' looks like a value that belongs to the '{match_attr}' attribute. \n  Please specify the value fully, as something like {match_attr}={search_val}."
                                else:
                                    warn_msg = f"\n- The input attribute '{clause.attribute}' does not exist in the DataFrame. \n  Please check your input intent for typos."
                        if clause.value != "" and clause.attribute != "" and clause.filter_op == "=":
                            # Skip check for NaN filter values
                            if not solas.utils.utils.like_nan(clause.value):
                                series = ldf[clause.attribute]
                                if not is_datetime_series(series):
                                    if isinstance(clause.value, list):
                                        vals = clause.value
                                    else:
                                        vals = [clause.value]
                                    for val in vals:
                                        if (
                                            solas.config.executor.name == "PandasExecutor"
                                            and val not in series.values
                                        ):
                                            warn_msg = f"\n- The input value '{val}' does not exist for the attribute '{clause.attribute}' for the DataFrame."
            return warn_msg, g_mark_type

        warn_msg = ""
        first_mark_type = ""
        for clause in intent:
            if type(clause) is list:
                for s in clause:
                    warn_msg_new, mark_type = validate_clause(s, first_mark_type)
                    warn_msg += warn_msg_new
                    first_mark_type = mark_type
            else:
                warn_msg_new, mark_type = validate_clause(clause, first_mark_type)
                warn_msg += warn_msg_new
                first_mark_type = mark_type
        if warn_msg != "" and not suppress_warning:

            warnings.warn(
                "\nThe following issues are ecountered when validating the parsed intent:" + warn_msg,
                stacklevel=2,
            )
        return warn_msg == ""
