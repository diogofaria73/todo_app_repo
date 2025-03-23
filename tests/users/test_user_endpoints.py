from http import HTTPStatus

from todo_api.domains.users.schemas.UserSchema import (
    UserSchemaPublic,
)
from todo_api.repositories.models.database_models import User


def test_create_user(session):
    # Create a new user
    user = User(
        username='test_user',
        first_name='teste',
        last_name='teste',
        email='test_email@gmail.com',
        password='test_password',
    )

    # Add the user to the session
    session.add(user)

    # Commit the transaction
    session.commit()

    # Query database to retry created register
    user = session.query(User).filter_by(username='test_user').first()

    # Assert the user was created correctly
    assert user.id == 1
    assert user.username == 'test_user'
    assert user.first_name == 'teste'
    assert user.last_name == 'teste'
    assert user.email == 'test_email@gmail.com'
    assert user.password == 'test_password'


def test_read_users_schema(client):
    response = client.get('/users')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': []}


def test_read_not_found_user_by_id(client, user):
    response = client.get('/users/2')

    user_schema = UserSchemaPublic.model_validate(user).model_dump()

    if not user_schema:
        assert response.status_code == HTTPStatus.NOT_FOUND
        assert response.json() == {'detail': 'User not found.'}


def test_read_user_by_id(client, user):
    response = client.get('/user/by_id/1')
    user_schema = UserSchemaPublic.model_validate(user).model_dump()

    assert response.status_code == HTTPStatus.OK
    assert response.json() == user_schema


def test_read_users_with_user(client, user):
    response = client.get('/users')
    user_schema = UserSchemaPublic.model_validate(user).model_dump()

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': [user_schema]}


def test_update_user(client, user):
    response = client.put(
        '/users/1',
        json={
            'username': 'new_username',
            'first_name': 'new_first_name',
            'last_name': 'new_last_name',
            'email': 'new@teste.com',
            'password': 'new_password',
        },
    )

    assert response.status_code == HTTPStatus.OK

    assert response.json() == {
        'id': 1,
        'username': 'new_username',
        'first_name': 'new_first_name',
        'last_name': 'new_last_name',
        'email': 'new@teste.com',
    }


def test_delete_user(): ...
