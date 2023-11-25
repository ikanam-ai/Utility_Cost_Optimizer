import streamlit as st
import hydralit_components as hc
from streamlit_javascript import st_javascript
from streamlit_echarts import st_echarts
from utils.train import all_logic


def teach():
    dataframe = st.session_state.dataframe
    st.columns([0.2, 0.6, 0.2])[1].title("Обучаем модель...")

    with hc.HyLoader('', hc.Loaders.pulse_bars):
        st.session_state.predict_result = all_logic(dataframe)

    st.toast("Модель обучена!", icon="✅")
    st.session_state.i_step = "a"
    # # хак для обновления таббара
    st_javascript("""setTimeout(() => {});""")


def stry(selected):
    st.session_state.i_selected = selected
    st.session_state.i_step = "b"


def sm():
    selected_ = st.session_state.get("i_selected", [])
    dataframe = st.session_state.dataframe
    selected = st.multiselect("Выберите переменные X:", dataframe.columns, placeholder="Выберите", default=selected_)
    st.columns(3)[1].button("Применить", key="dsgs", on_click=lambda x=selected: stry(x), use_container_width=True)


def steps():
    step = st.session_state.get('i_step')
    if step is None:
        teach()
    elif step == "a":
        sm()
    else:
        sm()
        selected = st.session_state.get("i_selected", [])
        if selected:
            dataframe = st.session_state.dataframe
            data = dataframe[selected].corr()
            cols = [data[col].tolist() for col in data.columns]
            res = []
            for i, col in enumerate(cols):
                for j, item in enumerate(col):
                    res.append([i, j, item or "-"])
            heatmap(selected, res)


def heatmap(ox, data):
    option = {
        "tooltip": {"position": "top"},
        "grid": {"height": "50%", "top": "10%"},
        "xAxis": {"type": "category", "data": list(ox), "splitArea": {"show": True}},
        "yAxis": {"type": "category", "data": list(ox), "splitArea": {"show": True}},
        "visualMap": {
            "min": 0,
            "max": 1,
            "calculable": True,
            "orient": "horizontal",
            "left": "center",
            "bottom": "15%",
        },
        "series": [
            {
                "name": "",
                "type": "heatmap",
                "data": data,
                "label": {"show": True},
                "emphasis": {
                    "itemStyle": {"shadowBlur": 10, "shadowColor": "rgba(0, 0, 0, 0.5)"}
                },
            }
        ],
    }
    st_echarts(option, height="500px")


def main():
    st.title("Корреляция")
    steps()
