from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserSchemaPublic(BaseModel):
    id: int
    username: str
    email: EmailStr


class UserDb(UserSchema):
    id: int


class UserList(BaseModel):
    users: list[UserSchemaPublic]
