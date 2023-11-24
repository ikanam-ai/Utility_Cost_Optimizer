import streamlit as st
import numpy as np
import pandas as pd


def main():
    st.subheader("Выбросы")
    chart_data = pd.DataFrame(
        {
            "col1": np.random.randn(20),
            "col2": np.random.randn(20),
            "col3": np.random.choice(["A", "B", "C"], 20),
        }
    )

    st.area_chart(chart_data, x="col1", y="col2", color="col3")
