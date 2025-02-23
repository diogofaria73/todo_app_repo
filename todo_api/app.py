from http import HTTPStatus

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import or_, select

from todo_api.domains.users.schemas.UserSchema import (
    UserList,
    UserSchema,
    UserSchemaPublic,
)
from todo_api.repositories.database import get_session
from todo_api.repositories.models.database_models import User

app = FastAPI()


@app.post(
    '/users/',
    status_code=HTTPStatus.CREATED,
    response_model=UserSchemaPublic,
    tags=['Users'],
)
def create_user(user: UserSchema, session=Depends(get_session)):
    user_exists = session.scalar(
        select(User).where(
            or_(User.email == user.email, User.username == user.username)
        )
    )

    if user_exists:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='User with the same email or username already exists.',
        )

    user = User(
        username=user.username,
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
        password=user.password,
    )

    session.add(user)
    session.commit()

    session.refresh(user)

    return user


@app.get('/users', response_model=UserList, tags=['Users'])
def read_users(limit: int = 5, session=Depends(get_session)):

    users = session.scalars(
        select(User).limit(limit)
    )

    return {'users': users}
