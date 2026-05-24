"""FAQ API routes."""

from fastapi import APIRouter

from app.models.myth_models import FAQRequest, FAQResponse
from app.services.myth_service import MythService

router = APIRouter(prefix="/faq", tags=["faq"])


@router.post("", response_model=FAQResponse)
async def faq(request: FAQRequest):
    service = MythService()
    return await service.answer_faq(request)
