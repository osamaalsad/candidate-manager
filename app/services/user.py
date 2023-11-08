from app.db import users_collection
from app.models.users import UserCreate


class UserService:
    @staticmethod
    async def create_user(user: UserCreate):
        user.hash_password()
        result = await users_collection.insert_one(user.model_dump())

        # Get the inserted user's ID
        inserted_id = result.inserted_id

        return {**user.model_dump(), "_id": str(inserted_id)}
