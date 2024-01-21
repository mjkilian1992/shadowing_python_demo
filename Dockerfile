# Common base image
FROM public.ecr.aws/docker/library/python:3.11-slim AS base

# python:
ENV PYTHONFAULTHANDLER=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONHASHSEED=random
# pip:
ENV PIP_NO_CACHE_DIR=off
ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV PIP_DEFAULT_TIMEOUT=100
# poetry:
ENV POETRY_VIRTUALENVS_CREATE=false
ENV POETRY_CACHE_DIR='/var/cache/pypoetry'

# System deps:
RUN apt-get update && apt-get install --no-install-recommends -y \
    bash \
    build-essential \
    curl \
    gettext \
    git \
    libpq-dev \
    wget \
  # Cleaning cache:
  && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/* \
  && pip install "poetry" && poetry --version

# set work directory
WORKDIR /app
COPY pyproject.toml poetry.lock /app/

# Install dependencies:
RUN poetry install --with dev
# copy project
COPY . .