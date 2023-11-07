from datetime import timedelta

from fastapi import HTTPException, APIRouter

from app.db import users_collection  # Import your user collection from the database module
from app.models.users import UserLogin
from app.security.jwt import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter()


@router.post("/token")
async def login_for_access_token(user_login: UserLogin):
    # Check if the email exists in the user collection (you might need to customize this logic)
    email = user_login.email
    user = await users_collection.find_one({"email": email})

    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    # If the email is valid, issue a JWT token
    user_data = {"sub": email}  # You can customize the payload as needed
    access_token = create_access_token(user_data, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    return {"access_token": access_token, "token_type": "bearer"}
