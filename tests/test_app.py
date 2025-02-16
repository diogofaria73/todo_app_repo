from http import HTTPStatus

from fastapi.testclient import TestClient


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'test_user',
            'email': 'teste@teste.com',
            'password': 'test_password',
        },
    )
    assert response.status_code == HTTPStatus.CREATED

    assert response.json() == {
        'username': 'test_user',
        'email': 'teste@teste.com',
        'password': 'test_password',
    }
