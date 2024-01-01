{%- set version_parts = cookiecutter.python_version.split(".") -%}
FROM python:{{ version_parts[0] + "." ~ version_parts[1] }}-slim-bookworm
WORKDIR /usr/src/app
COPY . /usr/src/app
RUN pip install -U pip && pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
