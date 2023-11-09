import unittest
from unittest.mock import patch, MagicMock
from app.services.user import UserService
from app.models.users import UserCreate


class TestUserService(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.mock_user_repository = patch("app.repositories.user.UserRepository").start()

    @classmethod
    def tearDownClass(cls):
        patch.stopall()

    def _create_mocked_instance(self):
        return MagicMock()

    def _get_mocked_user(self):
        return {
            "_id": "mocked_id",
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "password": "hashed_password",
        }

    def _get_mocked_user_create(self):
        return UserCreate(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            password="secretpassword"
        )

    @patch("app.repositories.user.UserRepository")
    async def test_create_user(self, mock_user_repository):
        mocked_instance = self._create_mocked_instance()
        mocked_instance.create_user.return_value = self._get_mocked_user()

        self.mock_user_repository.return_value = mocked_instance

        user_service = UserService()
        result = await user_service.create_user(user= self._get_mocked_user_create())

        self.assertEqual(result, self._get_mocked_user())
        mocked_instance.create_user.assert_called_once_with(self._get_mocked_user_create())

