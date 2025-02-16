from http import HTTPStatus
from typing import List

from fastapi import FastAPI

from todo_api.domains.users.schemas.UserSchema import (
    UserList, UserSchema, UserSchemaPublic, UserDb)

app = FastAPI()

database = []


@app.post(
    '/users',
    status_code=HTTPStatus.CREATED,
    response_model=UserSchemaPublic,
    tags=['Users'],
)
def create_user(user: UserSchema):
    user_with_id = UserDb(id=len(database) + 1, **user.model_dump())

    database.append(user_with_id)

    return user_with_id


@app.get(
    '/users',
    status_code=HTTPStatus.OK,
    response_model=UserList,
    tags=['Users'],
)
def read_users():

    return {'users': database}
