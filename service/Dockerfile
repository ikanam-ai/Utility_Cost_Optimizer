FROM python:3.10.4-slim-buster AS development_build

ENV STREAMLIT_PORT="7484"
ENV USER_LOGIN="login"
ENV USER_PASSWORD="password"

RUN apt-get -y update && apt-get -y upgrade && apt-get install -y ffmpeg
RUN pip install poetry
WORKDIR /app
COPY pyproject.toml poetry.lock /app/
COPY service/ /app/service
RUN poetry install
ENTRYPOINT ["poetry", "run", "start"]