from pydantic import BaseModel, EmailStr


class UserData(BaseModel):
    username: str
    email: EmailStr
    password: str
