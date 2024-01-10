from fastapi import FastAPI

from src.main import __version__


def test_app_instantiation(client):
    assert isinstance(client.app, FastAPI)


def test_version_number():
    assert __version__ == "{{cookiecutter.project_version}}"


def test_homepage_route_get_request(client):
    response = client.get("/")
    assert response.status_code == 200


def test_homepage_json_response_content(client):
    response = client.get("/")

    expected_response_body = {"hello": "world"}

    # JSONResponse returns text as string so we need to parse it into json format
    actual_response_body = response.json()

    # Assert that both responses match.
    assert actual_response_body == expected_response_body


def test_non_existent_route_error_status_code(client):
    response = client.get("/nonexistentroute")
    assert response.status_code == 404
