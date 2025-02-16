from http import HTTPStatus
from typing import List

from fastapi import FastAPI

from todo_api.domains.todos.schemas.TodoSchema import TodoSchema
from todo_api.domains.users.schemas.UserSchema import UserSchema, UserSchemaPublic

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK)
def read_root():
    return {'message': 'Hello, World!'}


@app.post(
    '/users', status_code=HTTPStatus.CREATED, response_model=UserSchema, tags=['Users']
)
def create_user(user: UserSchema):
    return user


@app.get('/users', status_code=HTTPStatus.OK, response_model=List[UserSchemaPublic], tags=['Users'])
def get_all_users():
    return []
