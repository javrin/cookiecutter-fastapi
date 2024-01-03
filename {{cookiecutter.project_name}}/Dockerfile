{%- set version_parts = cookiecutter.python_version.split(".") -%}
FROM python:{{ version_parts[0] + "." ~ version_parts[1] }}-slim-bookworm

ENV PIPX_HOME=/usr/local/py-utils \
    PIPX_BIN_DIR=/usr/local/py-utils/bin \
    PYTHONUSERBASE=/tmp/pip-tmp \
    PIP_CACHE_DIR=/tmp/pip-tmp/cache

ENV PATH=${PATH}:${PIPX_BIN_DIR}

RUN pip3 install --disable-pip-version-check --no-warn-script-location --no-cache-dir --user pipx
RUN /tmp/pip-tmp/bin/pipx install --pip-args=--no-cache-dir pipx && rm -rf /tmp/pip-tmp

ENV POETRY_HOME=/usr/local/py-utils

RUN ${PIPX_BIN_DIR}/pipx install --system-site-packages --pip-args '--no-cache-dir --force-reinstall' poetry==1.7.1

WORKDIR /app
COPY pyproject.toml poetry.lock ./

RUN ${PIPX_BIN_DIR}/poetry config virtualenvs.create false
RUN --mount=type=cache,target=/root/.cache/pypoetry/ ${PIPX_BIN_DIR}/poetry install --no-interaction --no-ansi --without dev

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
