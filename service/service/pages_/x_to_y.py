import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
from catboost import CatBoostRegressor
from streamlit_echarts import st_echarts
from utils.train import prepare_data, all_logic


def main():
    st.title("")
    params = st.session_state.get('data_params', [])
    result: tuple[
        pd.DataFrame, pd.DataFrame, pd.DataFrame, CatBoostRegressor, tuple[float, int]] = st.session_state.get(
        'predict_result')
    dataframe = st.session_state.dataframe
    selected = st.multiselect("Выберите переменные X:", dataframe.columns, placeholder="Выберите")
    model_metrics, feature_df = all_logic(dataframe, dataframe.columns)
    # model_metrics - 2 числа: [mae, smape] - нужно ы их написать
    # feature_df - датасет полезности фичей - вывести красивой таблицей
    st.write(dataframe[selected].corr())  # 0 график каралелограм
    # data = [
    #
    # ]
    #
    # option = {
    #     "tooltip": {"position": "top"},
    #     "grid": {"height": "50%", "top": "10%"},
    #     "xAxis": {"type": "category", "data": xs, "splitArea": {"show": True}},
    #     "yAxis": {"type": "category", "data": ys, "splitArea": {"show": True}},
    #     "visualMap": {
    #         "min": 0,
    #         "max": 10,
    #         "calculable": True,
    #         "orient": "horizontal",
    #         "left": "center",
    #         "bottom": "15%",
    #     },
    #     "series": [
    #         {
    #             "name": "",
    #             "type": "heatmap",
    #             "data": data,
    #             "label": {"show": True},
    #             "emphasis": {
    #                 "itemStyle": {"shadowBlur": 10, "shadowColor": "rgba(0, 0, 0, 0.5)"}
    #             },
    #         }
    #     ],
    # }
    # st_echarts(option, height="500px")
