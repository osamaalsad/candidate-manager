from fastapi.testclient import TestClient
from motor.motor_asyncio import AsyncIOMotorClient
from passlib.hash import pbkdf2_sha256

from main import app

client = TestClient(app)


def test_login_for_access_token():
    # Mock user data for testing
    test_user_data = {
        "first_name": "test",
        "last_name": "test",
        "email": "test@example.com",
        "password": pbkdf2_sha256.hash("test_password"),
    }

    # Insert the mock user data into the database
    mongo_client = AsyncIOMotorClient("mongodb://localhost:27017/")
    test_db = mongo_client["candidatemanagerdb"]
    test_users_collection = test_db["users"]
    test_users_collection.insert_one(test_user_data)

    # Perform the test
    response = client.post("/auth/token", json={"email": "test@example.com", "password": "test_password"})

    # Assert the response status code and token type
    assert response.status_code == 200
    assert response.json()["token_type"] == "bearer"

    # Clean up the test user data from the database
    test_users_collection.delete_one({"email": "test@example.com"})

# Run the tests using the command: pytest test_authentication_service.py
