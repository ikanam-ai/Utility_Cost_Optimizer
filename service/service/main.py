import streamlit as st
import streamlit_antd_components as sac
from pages_ import pages
from hacks.authenticate import Authenticate


def main() -> None:
    if 'index' not in st.session_state:
        st.session_state['index'] = 0

    with st.sidebar.container():
        menu = sac.menu(
            items=list(pages.keys()),
            index=st.session_state['index'],
            open_all=True,
            size='middle',
            format_func=lambda page: pages[page].title,
            indent=100
        )
        with st.sidebar.container():
            st.divider()
            st.info("Made with ❤ by the ikanam")
            authenticator: Authenticate = st.session_state.authenticator
            authenticator.logout(st, 'Выйти', 'sidebar', key='logout_')

    with st.container():
        if menu in pages:
            pages[menu].method()
