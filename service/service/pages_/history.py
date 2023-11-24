import streamlit as st
import streamlit_antd_components as sac
from utils.history import get_history, delete_history_item
from components.history_item import history_item


def main():
    st.subheader("История отчетов")
    history = get_history()
    if not history:
        st.info("История пока пуста, сохранить отчет можно после анализа")
        return
    total = len(history)
    page_size = 30
    page = sac.pagination(total=total, align='center', jump=True, show_total=True, page_size=page_size)
    slice = history[(page - 1) * page_size: page * page_size]
    cols_count = 3
    cols = st.columns(cols_count)
    for i, item in enumerate(slice):
        history_item(cols[i % cols_count], item)
