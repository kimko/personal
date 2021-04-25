from fastapi import APIRouter, Depends

from app.config import Settings, get_settings

router = APIRouter()


@router.get("/ping")
async def ping(settings: Settings = Depends(get_settings)):
    return {"environment": settings.environment, "testing": settings.testing}
