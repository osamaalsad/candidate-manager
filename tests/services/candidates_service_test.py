import unittest
from unittest.mock import patch, MagicMock

from app.models.candidates import CandidateCreate
from app.services.candidates import CandidateService


class TestCandidateService(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.mock_candidates_repository = patch("app.repositories.candidates.CandidatesRepository").start()

    @classmethod
    def tearDownClass(cls):
        patch.stopall()

    def _create_mocked_instance(self):
        return MagicMock()

    def _get_mocked_candidate(self):
        return {
            "_id": "mocked_id",
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "career_level": "Senior",
            "job_major": "Computer Science",
            "years_of_experience": 5,
            "degree_type": "Bachelor",
            "skills": ["Python", "FastAPI"],
            "nationality": "US",
            "city": "New York",
            "salary": 80000.0,
            "gender": "Male",
        }

    def _get_mocked_candidates(self):
        return [
            {
                "_id": "mocked_id_1",
                "first_name": "John",
                "last_name": "Doe",
                "email": "john.doe@example.com",
                "career_level": "Senior",
                "job_major": "Computer Science",
                "years_of_experience": 5,
                "degree_type": "Bachelor",
                "skills": ["Python", "FastAPI"],
                "nationality": "US",
                "city": "New York",
                "salary": 80000.0,
                "gender": "Male",
            },
            {
                "_id": "mocked_id_2",
                "first_name": "Jane",
                "last_name": "Doe",
                "email": "jane.doe@example.com",
                "career_level": "Junior",
                "job_major": "Information Technology",
                "years_of_experience": 2,
                "degree_type": "Master",
                "skills": ["Java", "Spring"],
                "nationality": "Canada",
                "city": "Toronto",
                "salary": 60000.0,
                "gender": "Female",
            },
        ]

    def _get_mocked_candidate_create(self):
        return CandidateCreate(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            career_level="Senior",
            job_major="Computer Science",
            years_of_experience=5,
            degree_type="Bachelor",
            skills=["Python", "FastAPI"],
            nationality="US",
            city="New York",
            salary=80000.0,
            gender="Male",
        )

    async def test_create_candidate(self):
        mocked_instance = await self._create_mocked_instance()
        mocked_instance.create_candidate.return_value = await self._get_mocked_candidate()

        self.mock_candidates_repository.return_value = mocked_instance

        candidate_service = CandidateService()
        result = await candidate_service.create_candidate(candidate=await self._get_mocked_candidate_create())

        self.assertEqual(result, await self._get_mocked_candidate())
        mocked_instance.create_candidate.assert_called_once_with(await self._get_mocked_candidate_create())

    async def test_get_candidate(self):
        mocked_instance = await self._create_mocked_instance()
        mocked_instance.get_candidate.return_value = await self._get_mocked_candidate()

        self.mock_candidates_repository.return_value = mocked_instance

        candidate_service = CandidateService()
        result = await candidate_service.get_candidate(candidate_id="mocked_id")

        self.assertEqual(result, await self._get_mocked_candidate())
        mocked_instance.get_candidate.assert_called_once_with(candidate_id="mocked_id")

    async def test_update_candidate(self):
        mocked_instance = await self._create_mocked_instance()
        mocked_instance.update_candidate.return_value = await self._get_mocked_candidate()

        self.mock_candidates_repository.return_value = mocked_instance

        candidate_service = CandidateService()
        result = await candidate_service.update_candidate(
            candidate_id="mocked_id",
            updated_candidate=await self._get_mocked_candidate_create()
        )

        self.assertEqual(result, await self._get_mocked_candidate())
        mocked_instance.update_candidate.assert_called_once_with(
            candidate_id="mocked_id",
            updated_candidate=await self._get_mocked_candidate_create()
        )

    async def test_delete_candidate(self):
        mocked_instance = await self._create_mocked_instance()
        mocked_instance.delete_candidate.return_value = {"message": "Candidate deleted"}

        self.mock_candidates_repository.return_value = mocked_instance

        candidate_service = CandidateService()
        result = await candidate_service.delete_candidate(candidate_id="mocked_id")

        self.assertEqual(result, {"message": "Candidate deleted"})
        mocked_instance.delete_candidate.assert_called_once_with(candidate_id="mocked_id")

    async def test_get_all_candidate(self):
        mocked_instance = await self._create_mocked_instance()
        mocked_instance.get_all_candidate.return_value = await self._get_mocked_candidates()

        self.mock_candidates_repository.return_value = mocked_instance

        candidate_service = CandidateService()
        result = await candidate_service.get_all_candidate(search_keyword="Doe")

        self.assertEqual(result, await self._get_mocked_candidates())
        mocked_instance.get_all_candidate.assert_called_once_with(search_keyword="Doe")

