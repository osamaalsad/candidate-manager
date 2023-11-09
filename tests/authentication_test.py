from fastapi.testclient import TestClient
from motor.motor_asyncio import AsyncIOMotorClient

from src.app.services.auth import AuthenticationService
from src.main import app

client = TestClient(app)


def test_login_for_access_token():
    # Mock user data for testing
    test_user_data = {
        "email": "test@example.com",
        "password": "test_password",  # Replace with the actual hashed password for testing
    }

    # Insert the mock user data into the database
    mongo_client = AsyncIOMotorClient("mongodb://localhost:27017/")
    test_db = mongo_client["candidatemanagerdb"]
    test_users_collection = test_db["users"]
    test_users_collection.insert_one(test_user_data)

    # Create a login_user object for testing
    class MockLoginUser:
        def __init__(self, email, password):
            self.email = email
            self.password = password

    mock_login_user = MockLoginUser(email="test@example.com", password="test_password")

    # Perform the test
    response = client.post("/token", data={"username": "test@example.com", "password": "test_password"})

    # Assert the response status code and token type
    assert response.status_code == 200
    assert response.json()["token_type"] == "bearer"

    # Clean up the test user data from the database
    test_users_collection.delete_one({"email": "test@example.com"})

# Run the tests using the command: pytest test_authentication_service.py
