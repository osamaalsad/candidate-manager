from fastapi import APIRouter
from app.db import candidates_collection
from fastapi import Depends
from app.security.jwt import get_current_user

router = APIRouter()


@router.get("/all-candidates", response_model=list)
async def get_all_candidates(search_keyword: str = None, current_user: dict = Depends(get_current_user)):
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
