from fastapi import APIRouter

from app.models.users import UserCreate
from app.services.user import UserService

router = APIRouter()


@router.post("/users", response_model=UserCreate)
async def create_user(user: UserCreate):
    # Call the UserService to create the user
    created_user = await UserService.create_user(user)
    return created_user
