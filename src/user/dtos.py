from pydantic import BaseModel


class UserScheme(BaseModel):
    name: str
    username: str
    password: str
    email: str
