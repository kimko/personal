import logging
from typing import List, Union

from app.models.resume import Resume, ResumePayloadSchema

log = logging.getLogger("uvicorn")


async def post(payload: ResumePayloadSchema) -> int:
    resume = Resume(
        title=payload.title,
        shortDescription=payload.shortDescription,
        name=payload.name,
        email=payload.email,
        phone=payload.phone,
        public_id=payload.public_id,
    )
    await resume.save()
    return resume.id


async def get(id: int) -> Union[dict, None]:
    resume = await Resume.filter(id=id).first().values()
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
