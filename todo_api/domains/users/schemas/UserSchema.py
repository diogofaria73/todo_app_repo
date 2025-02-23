from pydantic import BaseModel, ConfigDict, EmailStr


class UserSchema(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: EmailStr
    password: str


class UserSchemaPublic(BaseModel):
    id: int
    username: str
    first_name: str
    last_name: str
    email: EmailStr
    model_config = ConfigDict(from_attributes=True)


class UserDb(UserSchema):
    id: int


class UserList(BaseModel):
    users: list[UserSchemaPublic]
