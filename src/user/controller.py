from sqlalchemy.orm import Session
from src.user.dtos import UserScheme
from src.user.models import UserModel
from fastapi import HTTPException
import jwt
from jwt.exceptions import InvalidTokenError
from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()


def get_password_hash(password):
    return password_hash.hash(password)


def register(body: UserScheme, db: Session):
    is_user = db.query(UserModel).filter(
        UserModel.username == body.username).first()
    if is_user:
        raise HTTPException(400, detail="username already exists")
    is_user = db.query(UserModel).filter(
        UserModel.email == body.email).first()
    if is_user:
        raise HTTPException(400, detail="email already exists")
    hash_password = get_password_hash(body.password)
    new_user = UserModel(name=body.name, username=body.username,
                         hash_password=hash_password, email=body.email)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
