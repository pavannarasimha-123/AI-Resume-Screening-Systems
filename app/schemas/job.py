from pydantic import BaseModel, Field


class JobSearchRequest(BaseModel):
    job_description: str = Field(..., min_length=20)


class ResumeMatch(BaseModel):
    resume_id: int
    file_name: str
    score: float

    matched_skills: list[str]

    missing_skills: list[str]

    recommendation: str


class JobSearchResponse(BaseModel):
    matches: list[ResumeMatch]