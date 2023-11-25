import streamlit as st
import streamlit_antd_components as sac
from utils.set_step import set_step


def set_params(params):
    st.session_state["data_params"] = params
    set_step("inner")
    st.session_state.index = 1


def choose_params():
    items = ['balance', 'area', "date_issued:year", "date_issued:month", "date_issued:day",
             "date_issued:day_of_week", "date_issued:day_of_year"]
    filtered = sac.transfer(
        items=items,
        titles=['Все доступные', 'Будут использоваться'],
        format_func='title',
        search=True,
        width="100%"
    )
    cols = st.columns(3)
    if filtered:
        cols[1].button("Применить", key="teach_btn", use_container_width=True, on_click=lambda: set_params(filtered))


def main():
    choose_params()
