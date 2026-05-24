"""Myth-check API routes."""

from fastapi import APIRouter

from app.models.myth_models import MythCheckRequest, MythCheckResponse
from app.services.myth_service import MythService

router = APIRouter(prefix="/myth-check", tags=["myth"])


@router.post("", response_model=MythCheckResponse)
async def myth_check(request: MythCheckRequest):
    service = MythService()
    return await service.check_myth(request)
