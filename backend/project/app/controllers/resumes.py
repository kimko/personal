import logging
from typing import List, Union

from app.models.resume import Resume, ResumePayloadSchema
from app.utils.factory import generate_payload

log = logging.getLogger("uvicorn")


async def post(payload: ResumePayloadSchema) -> int:
    resume = Resume(
        title=payload.title,
        short_description=payload.short_description,
        name=payload.name,
        email=payload.email,
        phone=payload.phone,
        public_id=payload.public_id,
        summary=payload.summary,
        jobs=payload.jobs,
        skills=payload.skills,
    )
    await resume.save()
    return resume.id


async def generate_random(public_id: str) -> Resume:
    random = generate_payload()
    random["public_id"] = public_id
    resume = Resume(**random)
    await resume.save()
    return resume


async def get(**kwargs) -> Union[dict, None]:
    if "public_id" in kwargs:
        resume = await Resume.filter(public_id=kwargs["public_id"]).first().values()
    else:
        resume = await Resume.filter(id=kwargs["id"]).first().values()
    if resume:
        return resume[0]
    return None


async def delete(id: int = 0) -> dict:
    if id:
        log.info(f"Delete {id}")
        await Resume.filter(id=id).first().delete()
    else:
        log.info("Delete All")
        count = await Resume.all().delete()
        return count


async def get_all() -> List:
    resumes = await Resume.all().values()
    return resumes
