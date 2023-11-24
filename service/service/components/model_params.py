import streamlit as st
from utils.set_step import set_step


def model_settings():
    months = [3, 6, 9, 12, 24, 36]
    current = st.session_state.get("data_month")
    index = months.index(current) if current else 0
    st.session_state["data_month"] = st.selectbox("Переиод в месяцах", months, placeholder="Выберите",
                                                  index=index)


def clear():
    set_step(None)
    st.session_state.index = 0


def model_params():
    st.button("🗑️ Очистить", key="clear_params", on_click=clear, use_container_width=True)
    params = st.session_state.get('data_params')
    if not params:
        st.text("Пусто")
    text = ""
    for i, p in enumerate(params):
        text += f"{i + 1}) {p}\n"
    st.text_area("Текущие параметры", value=text, disabled=True)
