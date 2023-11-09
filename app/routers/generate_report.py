from fastapi import APIRouter, Depends

from app.security.jwt import get_current_user
from app.services.reports import ReportService
router = APIRouter()


@router.get("/generate-report", dependencies=[Depends(get_current_user)])
async def generate_report():
    return await ReportService.generate_report()
