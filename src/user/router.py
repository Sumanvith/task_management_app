from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.utils.db import get_db
from src.user.dtos import UserScheme
from src.user import controller

user_routes = APIRouter(prefix="/user")


@user_routes.post("/register")
def register(body: UserScheme, db: Session = Depends(get_db), status_code=status.HTTP_201_CREATED):
    return controller.register(body, db)
