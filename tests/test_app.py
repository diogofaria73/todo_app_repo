from http import HTTPStatus

from fastapi.testclient import TestClient

from todo_api.app import app


def test_read_root_endpoint():
    client = TestClient(app)  # Arrange

    response = client.get('/')  # Act
    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Hello, world!'}  # Assert
