"""Contraceptives listing API."""

from typing import Optional

from fastapi import APIRouter, Query

from app.models.myth_models import ContraceptivesListResponse
from app.services.myth_service import MythService

router = APIRouter(prefix="/contraceptives", tags=["contraceptives"])


@router.get("", response_model=ContraceptivesListResponse)
async def list_contraceptives(
    language: str = Query("en"),
    category: Optional[str] = Query(None),
):
    service = MythService()
    return service.list_contraceptives(language=language, category=category)
