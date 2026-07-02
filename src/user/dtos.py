from pydantic import BaseModel


class UserScheme(BaseModel):
    name: str
    username: str
    password: str
    email: str


class UserResponseScheme(BaseModel):
    name: str
    username: str
    email: str
