import shap
import streamlit as st
import numpy as np
import pandas as pd
from catboost import CatBoostRegressor


def st_shap(plot, height=None):
    shap_html = f"<head>{shap.getjs()}</head><body>{plot.html()}</body>"
    # components.html(shap_html, height=height)


def main():
    st.subheader("Выбросы")
    result: tuple[
        pd.DataFrame, pd.DataFrame, pd.DataFrame, CatBoostRegressor, tuple[float, int]] = st.session_state.get(
        'predict_result')
    feature_df, y_pred, X, model, (mae, mae) = result
    chart_data = pd.DataFrame(
        {
            "col1": np.random.randn(20),
            "col2": np.random.randn(20),
            "col3": np.random.choice(["A", "B", "C"], 20),
        }
    )

    st.area_chart(chart_data, x="col1", y="col2", color="col3")
