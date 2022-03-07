FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY poetry.lock /app
COPY pyproject.toml /app
RUN pip install poetry
RUN poetry install
COPY . /app

RUN chmod +x ./docker-entrypoint.sh
ENTRYPOINT ./docker-entrypoint.sh