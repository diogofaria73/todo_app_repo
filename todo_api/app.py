from http import HTTPStatus

from fastapi import FastAPI

from todo_api.schemas import MessageSchema, UserSchema

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=MessageSchema, tags=['Root'])
def read_root():
    return {'message': 'Hello, world!'}


@app.post('/users', status_code=HTTPStatus.CREATED, response_model=UserSchema, tags=['Users'])
def create_user(user: UserSchema):
    return user
