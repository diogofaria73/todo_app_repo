from http import HTTPStatus

from fastapi import FastAPI

from todo_api.domains.users.schemas.UserSchema import (
    UserDb,
    UserList,
    UserSchema,
    UserSchemaPublic,
)

app = FastAPI()

database = []


@app.post(
    '/users/',
    status_code=HTTPStatus.CREATED,
    response_model=UserSchemaPublic,
    tags=['Users'],
)
def create_user(user: UserSchema):
    user_with_id = UserDb(id=len(database) + 1, **user.model_dump())

    database.append(user_with_id)

    return user_with_id


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


@app.delete('/users/{user_id}/', status_code=HTTPStatus.OK,
            response_model=UserSchemaPublic,
            tags=['Users'])
def delete_user(user_id: int):

    user_with_id = database[user_id - 1]
    del database[user_id - 1]

    return user_with_id
