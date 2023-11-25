import hydralit_components as hc
import streamlit as st
import streamlit_antd_components as sac
from streamlit_javascript import st_javascript
from utils.train import all_logic
from utils.set_step import set_step


def set_params(params):
    st.session_state["data_params"] = params
    set_step("teach")


def teach():
    params = st.session_state.get('data_params', [])
    dataframe = st.session_state.dataframe
    st.columns([0.2, 0.6, 0.2])[1].title("Обучаем модель...")

    with hc.HyLoader('', hc.Loaders.pulse_bars):
        st.session_state.predict_result = all_logic(dataframe, params)

    st.session_state["data_model"] = {}
    set_step("inner")
    st.toast("Модель обучена!", icon="✅")
    st.session_state.index = 1
    # хак для обновления таббара
    st_javascript("""setTimeout(() => {});""")


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
        cols[1].button("Обучить", key="teach_btn", use_container_width=True, on_click=lambda: set_params(filtered))


def main():
    step = st.session_state.get("step")
    if step == "teach":
        teach()
    elif step is None:
        choose_params()
