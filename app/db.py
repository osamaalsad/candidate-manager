# app/db.py
import motor.motor_asyncio

MONGO_URL = "mongodb://localhost:27017/"  # Replace with your MongoDB server URL

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
database = client["candidatemanagerdb"]  # Replace with your database name

# Define a collection for users
users_collection = database["users"]
candidates_collection = database["candidates"]