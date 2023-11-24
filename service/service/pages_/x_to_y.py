import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def main():
    st.title("Зависимость")
    np.random.seed(42)
    data = {
        "X1": np.random.rand(100),
        "X2": np.random.rand(100),
        "X3": np.random.rand(100),
        "X4": np.random.rand(100),
        "Y": np.random.rand(100)
    }

    df = pd.DataFrame(data)
    selected_y = st.selectbox("Выберите переменную Y:", df.columns, placeholder="Выберите")
    selected_x = st.multiselect("Выберите переменные X:", df.columns[:-1], placeholder="Выберите")
    st.write("Выбранные данные:")
    st.write(df)
    fig, ax = plt.subplots()
    for x in selected_x:
        ax.scatter(df[x], df[selected_y], label=x)

    ax.set_xlabel(selected_x)
    ax.set_ylabel(selected_y)
    ax.legend()
    st.pyplot(fig)
