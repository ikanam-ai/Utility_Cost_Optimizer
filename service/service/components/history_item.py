import streamlit as st
import os
from utils.history import get_history_item
from streamlit.delta_generator import DeltaGenerator


def show_more(item: os.DirEntry, data: str):
    ...


def history_item(place: DeltaGenerator, item: os.DirEntry):
    place.subheader(item.name)
    place.text(f"Дата создания: {item.stat().st_ctime}")
    data = get_history_item(item.name)
    place.download_button("Cкачать", key=f"download_{item.name}", data=data, file_name=item.name,
                          use_container_width=True)
    place.button("Подробнее", key=f"more_{item.name}", on_click=lambda: show_more(item, data),
                 use_container_width=True)
    place.divider()
