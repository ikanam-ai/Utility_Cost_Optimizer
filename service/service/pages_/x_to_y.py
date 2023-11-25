import shap
import pandas as pd
import streamlit as st
from catboost import CatBoostRegressor
import streamlit.components.v1 as components


def st_shap(plot, height=None):
    shap_html = f"<head>{shap.getjs()}</head><body>{plot.html()}</body>"
    components.html(shap_html, height=height)


def main():
    st.title("")
    params = st.session_state.get('data_params', [])
    result: tuple[pd.DataFrame, pd.DataFrame, CatBoostRegressor, tuple[float, int]] = st.session_state.get(
        'predict_result')
    feature_df, X, model, (mae, mae) = result

    selected_y = st.selectbox("Выберите переменную Y:", feature_df.columns, placeholder="Выберите")
    selected_x = st.multiselect("Выберите переменные X:", feature_df.columns[feature_df.columns != selected_y],
                                placeholder="Выберите")

    explainer = shap.TreeExplainer(model)
    shap_values = explainer(X)
    st_shap(shap.force_plot(shap_values))
