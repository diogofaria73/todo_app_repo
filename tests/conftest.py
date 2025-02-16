import pytest
from fastapi.testclient import TestClient

from todo_api import app


@pytest.fixture()
def client():
    return TestClient(app)
