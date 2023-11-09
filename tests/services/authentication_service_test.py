import unittest
from unittest.mock import patch, MagicMock
from fastapi import HTTPException
from app.services.auth import AuthenticationService
from app.models.users import UserLogin


class TestAuthenticationService(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.mock_users_collection = patch("app.db.connection.users_collection").start()
        cls.mock_create_access_token = patch("app.services.auth.create_access_token").start()

    @classmethod
    def tearDownClass(cls):
        patch.stopall()

    async def _create_mocked_instance(self):
        return MagicMock()

    async def _get_mocked_user(self):
        return {
            "_id": "mocked_id",
            "email": "john.doe@example.com",
            "password": "hashed_password",
        }

    async def _get_mocked_user_login(self, email="john.doe@example.com", password="secretpassword"):
        return UserLogin(email=email, password=password)

    @patch("app.db.connection.users_collection")
    @patch("app.services.auth.create_access_token")
    async def test_login_for_access_token(self, mock_users_collection, mock_create_access_token):
        mocked_instance = await self._create_mocked_instance()
        mocked_instance.find_one.return_value = await self._get_mocked_user()

        self.mock_users_collection.return_value = mocked_instance
        self.mock_create_access_token.return_value = "mocked_access_token"

        auth_service = AuthenticationService()
        result = await auth_service.login_for_access_token(login_user=await self._get_mocked_user_login())

        self.assertEqual(result, {"access_token": "mocked_access_token", "token_type": "bearer"})
        mocked_instance.find_one.assert_called_once_with({"email": "john.doe@example.com"})
        mock_create_access_token.assert_called_once_with({"sub": "john.doe@example.com"})

    @patch("app.db.connection.users_collection")
    async def test_login_with_incorrect_email(self, mock_users_collection):
        mocked_instance = await self._create_mocked_instance()
        mocked_instance.find_one.return_value = None

        self.mock_users_collection.return_value = mocked_instance

        auth_service = AuthenticationService()

        with self.assertRaises(HTTPException) as context:
            await auth_service.login_for_access_token(
                login_user=await self._get_mocked_user_login(email="nonexistent@example.com")
            )

        self.assertEqual(context.exception.status_code, 400)
        self.assertEqual(context.exception.detail, "Incorrect email or password")
        mocked_instance.find_one.assert_called_once_with({"email": "nonexistent@example.com"})

    @patch("app.db.connection.users_collection")
    async def test_login_with_incorrect_password(self, mock_users_collection):
        mocked_instance = await self._create_mocked_instance()
        mocked_instance.find_one.return_value = await self._get_mocked_user()

        self.mock_users_collection.return_value = mocked_instance

        auth_service = AuthenticationService()

        with self.assertRaises(HTTPException) as context:
            await auth_service.login_for_access_token(
                login_user=await self._get_mocked_user_login(password="incorrectpassword")
            )

        self.assertEqual(context.exception.status_code, 400)
        self.assertEqual(context.exception.detail, "Incorrect email or password")
        mocked_instance.find_one.assert_called_once_with({"email": "john.doe@example.com"})
