from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.schemas.resume import ResumeResponse
from app.services.resume_service import ResumeService

router = APIRouter(
    prefix="/api/v1/resumes",
    tags=["Resumes"]
)


@router.post(
    "/upload",
    response_model=ResumeResponse
)
def upload_resume(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    """
    Temporary user_id=1.
    Later we'll get it from JWT.
    """
    return ResumeService.save_resume(
        db,
        file,
        user_id=1
    )