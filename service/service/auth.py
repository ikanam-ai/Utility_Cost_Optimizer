import streamlit as st
import streamlit_authenticator as stauth
from hacks.authenticate import Authenticate

from config import Config
from main import main as main_

config = Config()

st.set_page_config(page_title="Ikanam")

authenticator = Authenticate(
    {
        "usernames": {
            config.USER_LOGIN: {
                "email": "ikanam@gmail.com",
                "name": "Ikanam it's me",
                "password": stauth.Hasher([config.USER_PASSWORD]).generate()[0]
            }
        }
    },
    "some_cookie_name",
    "some_signature_key",
    30,
    []
)

st.session_state.authenticator = authenticator

name, authentication_status, username = authenticator.login("Авторизация", "main")

custom_styles = """
    div[data-testid="stSidebarUserContent"] {
        padding: 6rem 1.5rem 0rem 1.5rem;
    }
"""

st.markdown(f'<style>{custom_styles}</style>', unsafe_allow_html=True)


if st.session_state["authentication_status"]:
    main_()
elif st.session_state["authentication_status"] is False:
    st.error("Пароль или логин введены неверно")
elif st.session_state["authentication_status"] is None:
    st.warning("Нужно ввести логин и пароль")
