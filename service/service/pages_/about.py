import streamlit as st


def main():
    st.title("О решении")
    st.markdown(r"""

**Архитектура решения**
**Технологии**

- **Нейронные сети**: Pytorch, TorchVision, Scikit-learn
- **Визуализация аналитики**: Plotly
- **Веб-приложение**: Streamlit

**Структура репозитория**

- service/: Код сервиса для отображения аналитики

**Использование**

+ 1 вариант, без docker
    - Клонировать репозиторий: git clone https://github.com/ikanam-ai/Utility_Cost_Optimizer.git
    - Установить зависимости в директории service: poetry install
    - Запустить приложение: poetry run start
+ 2 вариант, в docker
    - Клонировать репозиторий: git clone https://github.com/ikanam-ai/Utility_Cost_Optimizer.git
    - запустить приложение из docker-compose: docker-compose up

*Список всех переменных окружения:

```
STREAMLIT_PORT: Порт работы приложения
USER_LOGIN: Логин для авторизации в приложении
USER_PASSWORD: Пароль для авторизации в приложении
```

*Дефотные данные для входа:

- Логин: ikanam
- Пароль: ikanamForever""")
