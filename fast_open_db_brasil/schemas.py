from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserDB(UserSchema):
    user_id: int


class UserPublic(BaseModel):
    user_id: int
    username: str
    email: EmailStr


class UserListPublic(BaseModel):
    users: list[UserPublic]
