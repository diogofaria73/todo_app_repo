from todo_api.repositories.models.database_models import User


def test_create_user_db(session):
    # Create a new user
    user = User(
        username='test_user', email='test_email@gmail.com', password='test_password'
    )

    # Add the user to the session
    session.add(user)

    # Commit the transaction
    session.commit()

    # Query database to retry created register
    user = session.query(User).filter_by(username='test_user').first()

    # Assert the user was created correctly
    assert user.username == 'test_user'
    assert user.email == 'test_email@gmail.com'
    assert user.password == 'test_password'
