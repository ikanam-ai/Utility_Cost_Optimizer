import streamlit as st
import streamlit_authenticator as stauth
from hacks.authenticate import Authenticate
from utils.load_model import load_model

from config import Config
from main import main as main_

config = Config()


@st.cache_data
def load():
    return load_model()


st.set_page_config(page_title="Ikanam")

st.session_state.dataframe = load()

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

if st.session_state.get("authentication_status"):
    main_()
elif st.session_state.get("authentication_status") is False:
    st.error("Пароль или логин введены неверно")
elif st.session_state.get("authentication_status") is None:
    st.warning("Нужно ввести логин и пароль")
