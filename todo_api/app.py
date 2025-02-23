from http import HTTPStatus

from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, or_, select
from sqlalchemy.orm import Session

from todo_api.domains.users.schemas.UserSchema import (
    UserDb,
    UserList,
    UserSchema,
    UserSchemaPublic,
)
from todo_api.repositories.models.database_models import User
from todo_api.settings import Settings

app = FastAPI()

database = []


@app.post(
    '/users/',
    status_code=HTTPStatus.CREATED,
    response_model=UserSchemaPublic,
    tags=['Users'],
)
def create_user(user: UserSchema):

    service_db = create_engine(Settings().DATABASE_URL)

    with Session(service_db) as session:
        user_exists = session.scalar(
            select(User)
            .where(or_(User.username == user.username, User.email == user.email))
        )

        if user_exists:
            raise HTTPException(detail='User already exists. Please user another username or email.',
                                status_code=HTTPStatus.BAD_REQUEST)

        user = User(username=user.username, first_name=user.first_name,
                    last_name=user.last_name, email=user.email,
                    password=user.password)

        session.add(user)
        session.commit()

        session.refresh(user)

        return user


@app.get(
    '/users/',
    status_code=HTTPStatus.OK,
    response_model=UserList,
    tags=['Users'],
)
def read_users():
    return {'users': database}


@app.put(
    '/users/{user_id}/',
    status_code=HTTPStatus.OK,
    response_model=UserSchemaPublic,
    tags=['Users'],
)
def update_user(user_id: int, user: UserSchema):
    user_with_id = UserDb(**user.model_dump(), id=user_id)

    database[user_id - 1] = user_with_id

    return user_with_id


@app.delete(
    '/users/{user_id}/',
    status_code=HTTPStatus.OK,
    response_model=UserSchemaPublic,
    tags=['Users'],
)
def delete_user(user_id: int):
    user_with_id = database[user_id - 1]
    del database[user_id - 1]

    return user_with_id
