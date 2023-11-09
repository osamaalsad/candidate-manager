from app.models.users import UserCreate
from app.repositories.user import UserRepository


class UserService:
    @staticmethod
    async def create_user(user: UserCreate):
        return await UserRepository.create_user(user)

