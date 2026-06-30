from pydantic import BaseModel


class CandidateResponse(BaseModel):

    resume_id: int

    file_name: str

    score: float

    recommendation: str