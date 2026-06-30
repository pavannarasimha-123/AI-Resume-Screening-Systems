from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

from app.services.export_service import ExportService

router = APIRouter(
    prefix="/api/v1/jobs",
    tags=["Export"]
)


@router.get("/export")
def export_results():

    file_name = ExportService.export_csv()

    if not file_name:

        raise HTTPException(
            status_code=404,
            detail="No ranking results found"
        )

    return FileResponse(
        path=file_name,
        filename=file_name,
        media_type="text/csv"
    )