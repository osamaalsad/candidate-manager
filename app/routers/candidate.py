from fastapi import APIRouter, Depends

from app.models.candidates import CandidateCreate
from app.security.jwt import get_current_user
from app.services.candidates import CandidateService

router = APIRouter()
candidate_service = CandidateService()


@router.post("/candidates", response_model=CandidateCreate, dependencies=[Depends(get_current_user)])
async def create_candidate(candidate: CandidateCreate):
    return await candidate_service.create_candidate(candidate)


@router.get("/candidates/{candidate_id}", response_model=CandidateCreate, dependencies=[Depends(get_current_user)])
async def get_candidate(candidate_id: str):
    return await candidate_service.get_candidate(candidate_id)


@router.put("/candidates/{candidate_id}", response_model=CandidateCreate, dependencies=[Depends(get_current_user)])
async def update_candidate(
        candidate_id: str,
        updated_candidate: CandidateCreate,
        current_user: dict = Depends(get_current_user)
):
    return await candidate_service.update_candidate(candidate_id, updated_candidate)


@router.delete("/candidates/{candidate_id}", dependencies=[Depends(get_current_user)])
async def delete_candidate(candidate_id: str):
    return await candidate_service.delete_candidate(candidate_id)


@router.get("/all-candidates", response_model=list, dependencies=[Depends(get_current_user)])
async def get_all_candidates(search_keyword: str = None):
    return await candidate_service.get_all_candidate(search_keyword)
