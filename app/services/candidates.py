from fastapi import HTTPException

from app.repositories.candidates import CandidatesRepository
from app.models.candidates import CandidateCreate


class CandidateService:

    async def create_candidate(self, candidate: CandidateCreate):
        return await CandidatesRepository.create_candidate(candidate)

    async def get_candidate(self, candidate_id: str):
        result = await CandidatesRepository.get_candidate(candidate_id)
        if not result:
            raise HTTPException(status_code=404, detail="Candidate not found")

        return result

    async def update_candidate(self, candidate_id: str, updated_candidate: CandidateCreate):
        result = await CandidatesRepository.update_candidate(candidate_id, updated_candidate)
        if not result:
            raise HTTPException(status_code=404, detail="Candidate not found")

        return result

    async def delete_candidate(self, candidate_id: str):
        result = await CandidatesRepository.delete_candidate(candidate_id)
        if not result:
            raise HTTPException(status_code=404, detail="Candidate not found")

        return result

    async def get_all_candidate(self, search_keyword: str = None):
        return await CandidatesRepository.get_all_candidate(search_keyword)
