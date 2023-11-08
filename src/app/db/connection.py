# app/connection.py
import motor.motor_asyncio
from app.project.config import settings

client = motor.motor_asyncio.AsyncIOMotorClient(str(settings.MONGO_DSN))
database = client["candidatemanagerdb"]  # Replace with your database name

# Define a collection for users
users_collection = database["users"]
candidates_collection = database["candidates"]