from pydantic import BaseModel


class CandidateSummaryResponse(
    BaseModel
):

    resume_id: int

    file_name: str

    summary: str

    strengths: list[str]

    missing_skills: list[str]

    recommendation: str