import pytest
from faker import Faker
from starlette.testclient import TestClient

from main import app

fake = Faker()
Faker.seed(1369)


@pytest.fixture(name="fake")
def fixture_fake():
    """Pass a seeded Faker instance as a fixture"""
    return fake


@pytest.fixture(name="client")
def fixture_client():
    return TestClient(app)
