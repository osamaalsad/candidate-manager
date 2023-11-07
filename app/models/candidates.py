from pydantic import BaseModel
from typing import List
from typing_extensions import Literal


class CandidateCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    career_level: str
    job_major: str
    years_of_experience: int
    degree_type: str
    skills: List[str]
    nationality: str
    city: str
    salary: float
    gender: Literal["Male", "Female", "Not Specified"]
