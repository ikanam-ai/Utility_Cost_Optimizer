import shap
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from catboost import CatBoostRegressor


def st_shap(plot, height=None):
    shap_html = f"<head>{shap.getjs()}</head><body>{plot.html()}</body>"
    # components.html(shap_html, height=height)


def main():
    st.subheader("Выбросы")
    result: tuple[
        pd.DataFrame, pd.DataFrame, pd.DataFrame, CatBoostRegressor, tuple[float, int]] = st.session_state.get(
        'predict_result')
    dataframe = st.session_state.dataframe
    df = pd.DataFrame(dataframe)
    df['area'].fillna(0, inplace=True)
    df = df[df['area'] != 0]
    df['Отношение'] = df['Отнесено'] / df['area']
    mean_ratio = df['Отношение'].mean()
    std_ratio = df['Отношение'].std()
    anomaly_threshold = 2
    df['Аномалия'] = (df['Отношение'] < mean_ratio - anomaly_threshold * std_ratio) | (
                df['Отношение'] > mean_ratio + anomaly_threshold * std_ratio)
    anomalous_df = df[df['Аномалия']]
    sorted_df = df.sort_values(by='Отношение')
    top_5_percent = sorted_df.tail(int(0.05 * len(sorted_df)))
    bottom_5_percent = sorted_df.head(int(0.05 * len(sorted_df)))
    st.title('Таблицы аномалий')
    st.write('Топ 5% верхних значений:')
    st.write(top_5_percent)

    st.write('Топ 5% нижних значений:')
    st.write(bottom_5_percent)
