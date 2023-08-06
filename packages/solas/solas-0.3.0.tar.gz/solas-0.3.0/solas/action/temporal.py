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
from solas.vis.VisList import VisList
from solas.vis.Vis import Vis
import pandas as pd
from solas.core.frame import SolasDataFrame
from solas.interestingness.interestingness import interestingness
from solas.utils import utils


def temporal(ldf, **kwargs):
    """
    Generates line charts for temporal fields at different granularities.
    Parameters
    ----------
    ldf : solas.core.frame
            SolasDataFrame with underspecified intent.
    Returns
    -------
    recommendations : Dict[str,obj]
            Object with a collection of visualizations that result from the Temporal action.
    """
    vlist = []
    recommendation = {
        "action": "Temporal",
        "description": "Show trends over <p class='highlight-descriptor'>time-related</p> attributes.",
        "long_description": "Temporal displays line charts for all attributes related to datetimes in the dataframe.",
    }
    for c in ldf.columns:
        if ldf.data_type[c] == "temporal":
            try:
                generated_vis = create_temporal_vis(ldf, c)
                vlist.extend(generated_vis)
            except:
                pass

    # If no temporal visualizations were generated via parsing datetime, fallback to default behavior.
    if len(vlist) == 0:
        intent = [solas.Clause("?", data_type="temporal")]
        intent.extend(utils.get_filter_specs(ldf._intent))
        vlist = VisList(intent, ldf)
        for vis in vlist:
            vis.score = interestingness(vis, ldf)
    else:
        vlist = VisList(vlist)
        recommendation["long_description"] += (
            " Solas displays the overall temporal trend first,"
            + " followed by trends across other timescales (e.g., year, month, week, day)."
        )

    # Doesn't make sense to generate a line chart if there is less than 3 datapoints (pre-aggregated)
    if len(ldf) < 3:
        recommendation["collection"] = []
        return recommendation

    col_order = ldf.history.get_implicit_intent(ldf.columns)
    vlist.sort(intent_cols=col_order)
    vlist.filter(**kwargs)
    recommendation["collection"] = vlist
    return recommendation


def create_temporal_vis(ldf, col):
    """
    Creates and populates Vis objects for different timescales in the provided temporal column.
    Parameters
    ----------
    ldf : solas.core.frame
            SolasDataFrame with underspecified intent.

    col : str
            Name of temporal column.

    Returns
    -------
    vlist : [Vis]
            Collection of Vis objects.
    """
    formatted_date = pd.to_datetime(ldf[col], format="%Y-%m-%d")

    overall_vis = Vis([solas.Clause(col, data_type="temporal")], source=ldf, score=5)

    year_col = col + " (year)"
    year_df = SolasDataFrame({year_col: pd.to_datetime(formatted_date.dt.year, format="%Y")})
    year_vis = Vis([solas.Clause(year_col, data_type="temporal")], source=year_df, score=4)

    month_col = col + " (month)"
    month_df = SolasDataFrame({month_col: formatted_date.dt.month})
    month_vis = Vis(
        [solas.Clause(month_col, data_type="temporal", timescale="month")], source=month_df, score=3
    )

    day_col = col + " (day)"
    day_df = SolasDataFrame({day_col: formatted_date.dt.day})
    day_df.set_data_type(
        {day_col: "nominal"}
    )  # Since day is high cardinality 1-31, it can get recognized as quantitative
    day_vis = Vis([solas.Clause(day_col, data_type="temporal", timescale="day")], source=day_df, score=2)

    week_col = col + " (day of week)"
    week_df = solas.SolasDataFrame({week_col: formatted_date.dt.dayofweek})
    week_vis = Vis(
        [solas.Clause(week_col, data_type="temporal", timescale="day of week")], source=week_df, score=1
    )

    unique_year_values = len(year_df[year_col].unique())
    unique_month_values = len(month_df[month_col].unique())
    unique_week_values = len(week_df[week_col].unique())
    vlist = []

    vlist.append(overall_vis)
    if unique_year_values != 1:
        vlist.append(year_vis)
    if unique_month_values != 1:
        vlist.append(month_vis)
    if unique_week_values != 1:
        vlist.append(week_vis)
    return vlist
