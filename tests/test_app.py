from http import HTTPStatus

from fastapi.testclient import TestClient

from todo_api.app import app
from todo_api.domains.users.schemas.UserSchema import UserSchema

client = TestClient(app)


def test_read_root():
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello, World!'}


def test_create_user(user: UserSchema):
    user = UserSchema({
        'username': 'test',
        'email': 'test@example.com',
        'password': 'password',
    })
    response = client.post('/users', user)

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {user}
