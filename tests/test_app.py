from http import HTTPStatus


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
        'id': 1,
    }


def test_read_user(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK

    assert response.json() == {
        'users': [{'username': 'test_user', 'email': 'teste@teste.com', 'id': 1}]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'password': 'new_password',
            'username': 'test_user_updated',
            'email': 'new@updated.com',
            'id': 1
        },
    )

    assert response.json() == {
        'username': 'test_user_updated',
        'email': 'new@updated.com',
        'id': 1
    }


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK

    assert response.json() == {
        'username': 'test_user_updated',
        'email': 'new@updated.com',
        'id': 1
    }
