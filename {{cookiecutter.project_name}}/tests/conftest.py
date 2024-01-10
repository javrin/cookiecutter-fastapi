import pytest
from faker import Faker
from fastapi.testclient import TestClient

from src.main import app

fake = Faker()
Faker.seed(1369)


@pytest.fixture(name="fake")
def fixture_fake():
    """Pass a seeded Faker instance as a fixture"""
    return fake


@pytest.fixture(name="client")
def fixture_client():
    with TestClient(app) as test_client:
        yield test_client
