from bson import ObjectId
from fastapi import HTTPException

from app.db.connection import candidates_collection
from app.models.candidates import CandidateCreate


class CandidatesRepository:


    @staticmethod
    async def create_candidate(candidate: CandidateCreate):
        # Insert the candidate data into MongoDB
        result = await candidates_collection.insert_one(candidate.model_dump())

        # Get the inserted candidate's ID
        inserted_id = result.inserted_id

        return CandidateCreate(**candidate.model_dump(), _id=str(inserted_id))


    @staticmethod
    async def get_candidate(candidate_id: str):
        candidate = await candidates_collection.find_one({"_id": ObjectId(candidate_id)})
        return CandidateCreate(**{**candidate, "_id": str(candidate.pop("_id"))})

    @staticmethod
    async def update_candidate(candidate_id: str, updated_candidate: CandidateCreate):
        # Update the candidate data in MongoDB
        result = await candidates_collection.update_one(
            {"_id": ObjectId(candidate_id)}, {"$set": updated_candidate.model_dump()}
        )

        if result.modified_count:
            return updated_candidate

        return None

    @staticmethod
    async def delete_candidate(candidate_id: str):
        result = await candidates_collection.delete_one({"_id": ObjectId(candidate_id)})

        if result.deleted_count:
            return {"message": "Candidate deleted"}

        return None

    @staticmethod
    async def get_all_candidate(search_keyword: str = None):
        query = {}  # Empty query to retrieve all candidates

        if search_keyword:
            # Create a query to search for the keyword in all candidate fields
            query = {
                "$or": [
                    {"first_name": {"$regex": search_keyword, "$options": "i"}},
                    {"last_name": {"$regex": search_keyword, "$options": "i"}},
                    {"email": {"$regex": search_keyword, "$options": "i"}},
                    {"career_level": {"$regex": search_keyword, "$options": "i"}},
                    {"job_major": {"$regex": search_keyword, "$options": "i"}},
                    {"nationality": {"$regex": search_keyword, "$options": "i"}},
                    {"city": {"$regex": search_keyword, "$options": "i"}},
                ]
            }

        candidates = []

        async for candidate in candidates_collection.find(query):
            candidates.append({**candidate, "_id": str(candidate.pop("_id"))})

        return candidates
