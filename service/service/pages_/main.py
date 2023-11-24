import time
import streamlit as st
import streamlit_antd_components as sac
import hydralit_components as hc
from utils.set_step import set_step
from streamlit_javascript import st_javascript


def set_params(params):
    st.session_state["data_params"] = params
    set_step("teach")


def teach():
    params = st.session_state["data_params"]
    st.columns([0.2, 0.6, 0.2])[1].title("Обучаем модель...")

    with hc.HyLoader('', hc.Loaders.pulse_bars):
        time.sleep(2)
    st.session_state["data_model"] = {}
    set_step("inner")
    st.toast("Модель обучена!", icon="✅")
    st.session_state.index = 1
    # хак для обновления таб бара
    st_javascript("""setTimeout(() => {});""")


def choose_params():
    items = [f'item{i}' for i in range(30)]
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
