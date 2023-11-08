from datetime import timedelta

from fastapi import HTTPException, APIRouter, Depends
from fastapi.security import HTTPBearer

from app.db import users_collection  # Import your user collection from the database module
from app.models.users import UserLogin
from app.security.jwt import get_current_user
from app.services.auth import AuthenticationService

router = APIRouter()


@router.post("/token")
async def login_for_access_token(user: UserLogin):
    return await AuthenticationService.login_for_access_token(user)

