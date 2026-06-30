from fastapi import APIRouter

from app.services.candidate_service import CandidateService

router = APIRouter(
    prefix="/api/v1/candidates",
    tags=["Candidates"]
)


@router.get("/top")
def get_top_candidates():

    return {
        "candidates":
            CandidateService.get_top_candidates()
    }