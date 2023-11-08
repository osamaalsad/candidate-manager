from datetime import timedelta

from fastapi import HTTPException
from passlib.hash import pbkdf2_sha256

from app.db import users_collection
from app.security.jwt import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES


def verify_password(plain_password, hashed_password):
    return pbkdf2_sha256.verify(plain_password, hashed_password)


class AuthenticationService:

    @staticmethod
    async def login_for_access_token(login_user):
        email = login_user.email
        user = await users_collection.find_one({"email": email})
        if not user or not verify_password(login_user.password, user["password"]):
            raise HTTPException(status_code=400, detail="Incorrect email or password")

        # If the email is valid, issue a JWT token
        user_data = {"sub": email}  # You can customize the payload as needed
        access_token = create_access_token(user_data, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
        return {"access_token": access_token, "token_type": "bearer"}
