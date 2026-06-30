from pydantic import BaseModel


class DashboardStatsResponse(BaseModel):

    total_resumes: int

    highly_recommended: int

    recommended: int

    needs_review: int

    top_skill: str