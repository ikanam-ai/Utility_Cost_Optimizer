import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
from catboost import CatBoostRegressor
from streamlit_echarts import st_echarts
from utils.train import prepare_data, make_logic


def main():
    st.title("")
    params = st.session_state.get('data_params', [])
    result: tuple[
        pd.DataFrame, pd.DataFrame, pd.DataFrame, CatBoostRegressor, tuple[float, int]] = st.session_state.get(
        'predict_result')
    dataframe = st.session_state.dataframe
    feature_df, y, X, model, (mae, mae) = result
    X, y, processor = prepare_data(dataframe, dataframe.columns)
    selected = st.multiselect("Выберите переменные X:", processor.get_feature_names_out(), placeholder="Выберите")
    feature_df, y, X, model, model_metrics = make_logic(dataframe, selected)
    df_cor = pd.DataFrame(X, columns=processor.get_feature_names_out())
    df_cor['Отнесено'] = y
    ys = xs = ["Отнесено", *selected]
    st.write(df_cor[[*selected, "Отнесено"]].corr())
    data = [

    ]

    option = {
        "tooltip": {"position": "top"},
        "grid": {"height": "50%", "top": "10%"},
        "xAxis": {"type": "category", "data": xs, "splitArea": {"show": True}},
        "yAxis": {"type": "category", "data": ys, "splitArea": {"show": True}},
        "visualMap": {
            "min": 0,
            "max": 10,
            "calculable": True,
            "orient": "horizontal",
            "left": "center",
            "bottom": "15%",
        },
        "series": [
            {
                "name": "",
                "type": "heatmap",
                "data": data,
                "label": {"show": True},
                "emphasis": {
                    "itemStyle": {"shadowBlur": 10, "shadowColor": "rgba(0, 0, 0, 0.5)"}
                },
            }
        ],
    }
    st_echarts(option, height="500px")
