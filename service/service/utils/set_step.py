import streamlit as st


def set_step(step: str | None):
    st.session_state["step"] = step
