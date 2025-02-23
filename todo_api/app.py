from http import HTTPStatus

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import or_, select

from todo_api.domains.users.schemas.UserSchema import (
    UserList,
    UserSchema,
    UserSchemaPublic,
)
from todo_api.repositories.database import Session, get_session
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
def read_users(limit: int = 10, skip: int = 0, session=Depends(get_session)):
    users = session.scalars(select(User).limit(limit).offset(skip))

    return {'users': users}


@app.get('/user/by_id/{user_id}', response_model=UserSchemaPublic, tags=['Users'])
def read_user_by_id(user_id: int, session=Depends(get_session)):
    user = session.scalar(select(User).where(User.id == user_id))

    if not user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='User not found.',
        )

    return user


@app.put('/users/{user_id}', response_model=UserSchemaPublic, tags=['Users'])
def update_user(
    user_id: int, user: UserSchema, session: Session = Depends(get_session)
):
    db_user = session.scalar(select(User).where(User.id == user_id))

    if not db_user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='User not found.',
        )

    db_user.username = user.username
    db_user.email = user.email
    db_user.first_name = user.first_name
    db_user.last_name = user.last_name

    if user.password:
        db_user.password = user.password

    db_user.password = db_user.password

    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user


@app.delete('/users/{user_id}', response_model=UserSchemaPublic, tags=['Users'])
def delete_user(
    user_id: int, user: UserSchema, session: Session = Depends(get_session)
):
    db_user = session.scalar(select(User).where(User.id == user_id))

    if not db_user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='User not found.',
        )

    session.delete(db_user)
    session.commit()

    return {'user': db_user}
