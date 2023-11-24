import streamlit as st


def choose_params(options: list[str], on_submit):
    with st.container():
        st.header("Выберите элементы:")
        params = st.multiselect("Параметры", options, placeholder="Выберите")

        st.button('Обучение', use_container_width=True, on_click=lambda: on_submit(params), key="t_bt")
