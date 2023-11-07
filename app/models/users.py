# app/models.py
from pydantic import BaseModel


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: str


class UserLogin(BaseModel):
    email: str
