from fastapi import APIRouter
from pydantic import BaseModel

register_router = APIRouter()


class UserData(BaseModel):
    username: str
    email: str
    password: str


@register_router.post("/register")
def register(user: UserData):
    print(user.model_dump())
    return user
