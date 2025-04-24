ARG PYTHON_VERSION=python:3.13

FROM ${PYTHON_VERSION}-slim
ENV PYTHONPATH=/app:${PYTHONPATH}

WORKDIR /app
COPY . .
RUN pip install poetry && poetry config virtualenvs.create false && poetry install --without dev --no-root
