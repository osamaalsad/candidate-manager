from fastapi import APIRouter

from app.models.users import UserLogin
from app.services.auth import AuthenticationService

router = APIRouter()


@router.post("/token")
async def login_for_access_token(user: UserLogin):
    return await AuthenticationService.login_for_access_token(user)

