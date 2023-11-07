# app/routers/candidate.py
from bson import ObjectId
from fastapi import APIRouter, HTTPException
from fastapi import Depends

from app.db import candidates_collection
from app.models.candidates import CandidateCreate
from app.security.jwt import get_current_user

router = APIRouter()


@router.post("/candidates", response_model=CandidateCreate)
async def create_candidate(candidate: CandidateCreate, current_user: dict = Depends(get_current_user)):
    # Insert the candidate data into MongoDB
    result = await candidates_collection.insert_one(candidate.model_dump())

    # Get the inserted candidate's ID
    inserted_id = result.inserted_id

    return {**candidate.model_dump(), "_id": str(inserted_id)}


@router.get("/candidates/{candidate_id}", response_model=CandidateCreate)
async def get_candidate(candidate_id: str, current_user: dict = Depends(get_current_user)):
    print(f'ObjectId("{candidate_id}")')
    candidate = await candidates_collection.find_one({"_id": ObjectId(candidate_id)})

    if candidate:
        return {**candidate, "_id": str(candidate.pop("_id"))}
    else:
        raise HTTPException(status_code=404, detail="Candidate not found")


@router.put("/candidates/{candidate_id}", response_model=CandidateCreate)
async def update_candidate(
        candidate_id: str,
        updated_candidate: CandidateCreate,
        current_user: dict = Depends(get_current_user)
):
    # Update the candidate data in MongoDB
    result = await candidates_collection.update_one(
        {"_id": ObjectId(candidate_id)}, {"$set": updated_candidate.model_dump()}
    )

    if result.modified_count:
        return updated_candidate
    else:
        raise HTTPException(status_code=404, detail="Candidate not found")


@router.delete("/candidates/{candidate_id}")
async def delete_candidate(candidate_id: str, current_user: dict = Depends(get_current_user)):
    result = await candidates_collection.delete_one({"_id": ObjectId(candidate_id)})

    if result.deleted_count:
        return {"message": "Candidate deleted"}
    else:
        raise HTTPException(status_code=404, detail="Candidate not found")
