import logging
from typing import List

from fastapi import APIRouter, Depends, HTTPException

from app.controllers import resumes
from app.models.resume import ResumePayloadSchema, ResumeResponseSchema, ResumeSchema
from app.utils.auth import verify_token

router = APIRouter()
log = logging.getLogger("uvicorn")


@router.post(
    "/",
    response_model=ResumeResponseSchema,
    status_code=201,
    dependencies=[Depends(verify_token)],
)
async def create_resume(payload: ResumePayloadSchema) -> ResumeResponseSchema:
    resume_id = await resumes.post(payload)

    # TODO: this just returns the payload right now
    response_object = {
        "id": resume_id,
        "title": payload.title,
        # "shortDescription": payloa,
        "name": payload.name,
        # "email": str,
        # "phone": str,
        # "created_at": datetime,
        "public_id": payload.public_id,
        "summary": payload.summary,
        "jobs": payload.jobs,
        "skills": payload.skills,
    }
    return response_object


@router.post(
    "/random",
    response_model=ResumeSchema,
    status_code=201,
    dependencies=[Depends(verify_token)],
)
async def generate_random(public_id: str) -> ResumeSchema:
    log.info(f"Generate Random {public_id}")
    resume = await resumes.generate_random(public_id)
    return resume


@router.get("/{id}/", response_model=ResumeSchema, dependencies=[Depends(verify_token)])
async def read_resume(id: int) -> ResumeSchema:
    resume = await resumes.get(id=id)
    if not resume:
        raise HTTPException(status_code=404, detail="Resume not found")

    return resume


@router.get("/public/{public_id}/", response_model=ResumeSchema)
async def read_resume_public(public_id: str) -> ResumeSchema:
    resume = await resumes.get(public_id=public_id)
    if not resume:
        raise HTTPException(status_code=404, detail="Resume not found")

    return resume


@router.get(
    "/", response_model=List[ResumeSchema], dependencies=[Depends(verify_token)]
)
async def read_all_resumes() -> List[ResumeSchema]:
    return await resumes.get_all()


@router.delete(
    "/{id}/", response_model=ResumeResponseSchema, dependencies=[Depends(verify_token)]
)
async def delete_resume(id: int) -> ResumeResponseSchema:
    resume = await resumes.get(id=id)
    if not resume:
        raise HTTPException(status_code=404, detail="Resume not found")

    await resumes.delete(id)

    return resume


@router.delete("/", dependencies=[Depends(verify_token)])
async def delete_resumes(delete_all: bool = False) -> dict:
    if not delete_all:
        return {
            "message": "Nothing deleted. Set query parameter 'delete_all'",
            "deleted": 0,
        }

    count = await resumes.delete()

    return {"message": f"Deleted {count} resumes", "deleted": count}
