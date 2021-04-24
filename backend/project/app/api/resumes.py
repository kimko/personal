from fastapi import APIRouter, HTTPException

from app.api import crud
from app.models.pydantic import ResumePayloadSchema, ResumeResponseSchema


router = APIRouter()


@router.post("/", response_model=ResumeResponseSchema, status_code=201)
async def create_summary(payload: ResumePayloadSchema) -> ResumeResponseSchema:
    resume_id = await crud.post(payload)

    # TODO: this just returns the payload right now
    response_object = {
        "id": resume_id,
        "title": payload.title,
        # "shortDescription": payloa,
        "name": payload.name,
        # "email": str,
        # "phone": str,
        # "created_at": datetime,
        }
    return response_object
