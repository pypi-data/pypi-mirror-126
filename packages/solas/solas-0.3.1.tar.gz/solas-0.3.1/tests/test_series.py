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
from .context import solas
import pytest
import pandas as pd
import warnings


def test_df_to_series():
    # Ensure metadata is kept when going from df to series
    df = pd.read_csv("solas/data/car.csv")
    df._ipython_display_()  # compute metadata
    assert df.cardinality is not None
    series = df["Weight"]
    assert isinstance(series, solas.core.series.SolasSeries), "Derived series is type SolasSeries."
    print(df["Weight"]._metadata)
    assert df["Weight"]._metadata == [
        "_intent",
        "_inferred_intent",
        "_data_type",
        "unique_values",
        "cardinality",
        "_rec_info",
        "_min_max",
        "plotting_style",
        "_current_vis",
        "_widget",
        "_recommendation",
        "_prev",
        "_history",
        "_saved_export",
        "name",
        "_sampled",
        "_toggle_pandas_display",
        "_message",
        "_pandas_only",
        "pre_aggregated",
        "_type_override",
    ], "Metadata is lost when going from Dataframe to Series."
    assert df.cardinality is not None, "Metadata is lost when going from Dataframe to Series."
    assert series.name == "Weight", "Pandas Series original `name` property not retained."


def test_print_dtypes(global_var):
    df = pytest.college_df
    with warnings.catch_warnings(record=True) as w:
        print(df.dtypes)
        assert len(w) == 0, "Warning displayed when printing dtypes"


def test_print_iterrow(global_var):
    df = pytest.college_df
    with warnings.catch_warnings(record=True) as w:
        for index, row in df.iterrows():
            print(row)
            break
        assert len(w) == 0, "Warning displayed when printing iterrow"


def test_series_recommendation():
    df = pd.read_csv("https://raw.githubusercontent.com/lux/solas-datasets/master/data/employee.csv")
    df.plot_config = None
    df = df["YearsAtCompany"] / df["TotalWorkingYears"]
    assert len(df.recommendation["Distribution"]) > 0, "Recommendation property empty for SolasSeries"


def test_series_multivis_recommendation():
    covid = pd.read_csv(
        "https://github.com/lux/solas-datasets/blob/master/data/covid-stringency.csv?raw=True"
    )
    covid = covid.rename(columns={"stringency_index": "stringency"})
    covid["Day"] = pd.to_datetime(covid["Day"], format="%Y-%m-%d")
    series = covid["Day"]
    assert len(series.recommendation["Temporal"]) == 4, "Display 4 temporal vis based on `Day`"
    assert hasattr(series, "current_vis") == False


def test_unnamed_column():
    solas.config.plotting_backend = "matplotlib"
    df = pd.read_csv("https://raw.githubusercontent.com/lux/solas-datasets/master/data/employee.csv")
    solas.config.plotting_style = None
    series = df["YearsAtCompany"] / df["TotalWorkingYears"]
    series.__repr__()
    axis_title = "Series (binned)"
    exported_code_str = series.recommendation["Distribution"][0].to_matplotlib()
    assert axis_title in exported_code_str, "Unnamed column should have 'Series' as placeholder"

    solas.config.plotting_backend = "vegalite"
    series = df["YearsAtCompany"] / df["TotalWorkingYears"]
    series.__repr__()
    exported_code_str = series.recommendation["Distribution"][0].to_altair()
    assert axis_title in exported_code_str, "Unnamed column should have 'Series' as placeholder"
