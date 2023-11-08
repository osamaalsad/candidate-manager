# app/models.py
from pydantic import BaseModel
from passlib.hash import pbkdf2_sha256


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str

    def hash_password(self):
        self.password = pbkdf2_sha256.hash(self.password)


class UserLogin(BaseModel):
    email: str
    password: str