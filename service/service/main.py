import streamlit as st
import streamlit_antd_components as sac

from hacks.authenticate import Authenticate
from pages_ import pages
from components.model_params import model_params, model_settings


@st.cache_data
def get_children(step: str | None):
    if step != "inner":
        return [
            sac.MenuItem("main", icon="house-fill"),
        ]
    return [
        sac.MenuItem("main_with_children", icon="house-fill", children=[
            sac.MenuItem("x_to_y", icon="shuffle"),
            sac.MenuItem("emission", icon="bar-chart-line"),
            sac.MenuItem("map", icon="map"),
        ]),
    ]


def main() -> None:
    if "index" not in st.session_state:
        st.session_state["index"] = 0

    with st.sidebar.container():
        step = st.session_state.get("step")
        children = get_children(step)
        menu = sac.menu([
            *children,
            sac.MenuItem("history", icon="clock-history"),
            sac.MenuItem("about", icon="info-circle"),
        ],
            index=st.session_state["index"],
            open_all=True,
            size="middle",
            format_func=lambda page: pages[page].title if page in pages else page,
        )
        if step == "inner":
            with st.expander("⚙️ Настройки", expanded=True):
                model_settings()
        if step == "inner":
            with st.expander("🎚️ Параметры модели"):
                model_params()
        st.markdown("<br>", unsafe_allow_html=True)
        with st.sidebar.container():
            st.divider()
            st.info("Made with ❤ by ikanam")
            authenticator: Authenticate = st.session_state.authenticator
            authenticator.logout(st, "Выйти", "sidebar", key="logout_")

    with st.container():
        if menu in pages and pages[menu].method:
            pages[menu].method()
