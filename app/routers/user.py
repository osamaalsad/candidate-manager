from fastapi import APIRouter
from app.db import users_collection
from app.models.users import UserCreate

router = APIRouter()


@router.post("/users", response_model=UserCreate)
async def create_user(user: UserCreate):
    # Insert the user data into MongoDB
    result = await users_collection.insert_one(user.model_dump())

    # Get the inserted user's ID
    inserted_id = result.inserted_id

    return {**user.model_dump(), "_id": str(inserted_id)}
