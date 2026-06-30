from fastapi import APIRouter

from app.services.candidate_service import (
    CandidateService
)
from app.services.summary_service import (
    SummaryService
)

router = APIRouter(
    prefix="/api/v1/summary",
    tags=["AI Summary"]
)


@router.get("/{resume_id}")
def generate_summary(
    resume_id: int
):

    candidates = (
        CandidateService.get_top_candidates()
    )

    for candidate in candidates:

        if candidate["resume_id"] == resume_id:

            ai_result = (
                SummaryService.generate_summary(
                    candidate[
                        "matched_skills"
                    ],
                    candidate[
                        "missing_skills"
                    ]
                )
            )

            return {

                "resume_id":
                    candidate["resume_id"],

                "file_name":
                    candidate["file_name"],

                "summary":
                    ai_result["summary"],

                "strengths":
                    ai_result["strengths"],

                "missing_skills":
                    candidate[
                        "missing_skills"
                    ],

                "recommendation":
                    ai_result[
                        "recommendation"
                    ]
            }

    return {
        "error": "Resume not found"
    }