from fastapi import APIRouter
from app.services.reports import ReportService
router = APIRouter()


@router.get("/generate-report")
async def generate_report():
    return ReportService.generate_report()
