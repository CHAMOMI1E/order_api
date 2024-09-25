FROM python:3.12-alpine

LABEL authors="chamomile"

WORKDIR /EffectiveMobile_task

RUN apk add --no-cache \
    gcc \
    musl-dev \
    libffi-dev \
    openssl-dev \
    cargo \
    build-base

RUN apk add --no-cache curl

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:$PATH"

RUN poetry config virtualenvs.create false

COPY ./pyproject.toml ./poetry.lock* ./

RUN poetry install --no-root --no-interaction --no-ansi

COPY ./ ./

RUN chmod -R 777 ./
