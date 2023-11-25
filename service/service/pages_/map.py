import streamlit as st
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium


def create_popup(row):
    html = f"""<h3>{row['name']}</h3>
    <p>Год постройки: {row['year']}<br>
    Площадь: {row['area']}<br>
    Состояние: {row['state']}<br>
    ID объекта: {row['address_id']}<br>
    </p>"""
    iframe = folium.IFrame(html=html, width=500, height=300)
    popup = folium.Popup(iframe, max_width=2650)
    return popup


def main():
    st.title("Карта")
    df = pd.read_excel('models/FULL_adresses_data_RUS.xlsx')
    m = folium.Map(location=[60, 160], zoom_start=4)
    marker_cluster = MarkerCluster(name="Объекты").add_to(m)

    df.apply(lambda row: folium.Marker(
        location=[row['lat'], row['lng']],
        popup=create_popup(row)
    ).add_to(marker_cluster), axis=1)

    st_data = st_folium(m, width=725)
