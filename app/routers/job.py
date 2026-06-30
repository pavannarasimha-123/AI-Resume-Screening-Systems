from fastapi import APIRouter

from app.schemas.job import (
    JobSearchRequest,
    JobSearchResponse
)
from app.services.ranking_service import RankingService

router = APIRouter(
    prefix="/api/v1/jobs",
    tags=["AI Ranking"]
)


@router.post(
    "/search",
    response_model=JobSearchResponse
)
def search_job(request: JobSearchRequest):

    return RankingService.rank_resumes(
        request.job_description
    )