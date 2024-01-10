{%- set version_parts = cookiecutter.python_version.split(".") -%}
ARG PYTHON_VERSION={{ version_parts[0] + "." ~ version_parts[1] }}
ARG PYTHON_IMAGE_TAG=slim

###############################################################################
# PYTHON BASE IMAGE - Sets up Poetry env
###############################################################################
FROM python:${PYTHON_VERSION}-${PYTHON_IMAGE_TAG} as python-poetry-base

# Default to the latest version of Poetry
ARG POETRY_VERSION=""

ENV POETRY_VERSION=${POETRY_VERSION} \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1

ENV PATH="$POETRY_HOME/bin:$PATH"

###############################################################################
# POETRY BUILDER IMAGE - Installs Poetry (later copied to Runtime image)
###############################################################################
FROM python-poetry-base AS poetry-build

RUN apt-get update && \
    apt-get install --no-install-recommends -y curl
# Install Poetry via the official installer: https://python-poetry.org/docs/master/#installing-with-the-official-installer
# This script respects $POETRY_VERSION & $POETRY_HOME
RUN curl -sSL https://install.python-poetry.org | python3 -

###############################################################################
# PROJECT STAGE - Generate the project and copy poetry
###############################################################################
FROM python-poetry-base AS project

WORKDIR /app

COPY --from=poetry-build $POETRY_HOME $POETRY_HOME
COPY pyproject.toml poetry.lock ./

###############################################################################
# DEVELOPMENT RUNTIME STAGE - Used during development / testing
###############################################################################
FROM project as development

RUN --mount=type=cache,target=/root/.cache poetry install --no-root --with dev

COPY . .

EXPOSE 8000

CMD ["tail", "-f", "/dev/null"]

###############################################################################
# PRODUCTION RUNTIME STAGE - Final image used in production
###############################################################################
FROM project as production

RUN --mount=type=cache,target=/root/.cache poetry install --no-root --only main

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
