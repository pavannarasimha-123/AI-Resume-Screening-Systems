from fastapi import APIRouter

from app.schemas.dashboard import (
    DashboardStatsResponse
)
from app.services.dashboard_service import (
    DashboardService
)

router = APIRouter(
    prefix="/api/v1/dashboard",
    tags=["Dashboard"]
)


@router.get(
    "/stats",
    response_model=DashboardStatsResponse
)
def get_dashboard_stats():

    return DashboardService.get_stats()