import time

import streamlit as st

from components.choose_params import choose_params
from .emissions import main as emissions
from .map import main as map
from .x_to_y import main as x_to_y
from .report import main as report


def set_step(step):
    st.session_state['step'] = step


def default():
    def on_submit(params):
        st.session_state['data_params'] = params
        set_step("teach")

    choose_params([f"{i}" for i in range(20)], on_submit)


def teach():
    params = st.session_state['data_params']
    with st.spinner("Обучение, подождите.."):
        time.sleep(2)
    set_step("month")
    st.session_state['data_model'] = {}
    steps()


def month(place):
    def on_click(m):
        st.session_state['data_month'] = m

    months = [3, 6, 9, 12, 24, 36]
    place.subheader("Количество месяцев")
    current = st.session_state.get('data_month')
    cols = place.columns(2)
    for i, m in enumerate(months):
        cols[i % 2].checkbox(f'{m}', key=f"m_btn_{m}", on_change=lambda m=m: on_click(m),
                             value=m == current)


def plots():
    params = st.session_state['data_params']
    with st.expander("Используемые параметры"):
        for i, p in enumerate(params):
            st.text(f"{i + 1}) {p}")
    cols = st.columns(2)
    month(cols[0])
    col = cols[1]
    col.button("Зависимости параметров", key="x_to_y_btn", use_container_width=True,
               on_click=lambda: set_step('x_to_y'))
    col.button("Выбросы", key="emissions_btn", use_container_width=True, on_click=lambda: set_step('emissions'))
    col.button("Карта", key="map_btn", use_container_width=True, on_click=lambda: set_step('map'))
    col.button("Изменить параметры", key="change_p_btn", use_container_width=True, on_click=lambda: set_step(None))
    report_place = st.columns(1)[0]
    if st.session_state.step in ("emissions", "map", "x_to_y"):
        report_place.button("Отчет", key="report_btn", use_container_width=True, on_click=lambda: set_step("report"))


def steps():
    step = st.session_state.get('step')
    if step is None:
        default()
    elif step == 'teach':
        teach()
    else:
        plots()
        if step == 'x_to_y':
            x_to_y()
        elif step == 'map':
            map()
        elif step == 'emissions':
            emissions()
        elif step == 'report':
            report()


def main() -> None:
    st.title("Предсказание")
    steps()
