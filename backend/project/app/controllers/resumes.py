from typing import Union, List

from app.models.resume import Resume, ResumePayloadSchema


async def post(payload: ResumePayloadSchema) -> int:
    resume = Resume(
        title = payload.title,
        shortDescription = payload.shortDescription,
        name = payload.name,
        email = payload.email,
        phone = payload.phone,
    )
    await resume.save()
    return resume.id

async def get(id: int) -> Union[dict, None]:
    resume = await Resume.filter(id=id).first().values()
    if resume:
        return resume[0]
    return None

async def get_all() -> List:
    resumes = await Resume.all().values()
    return resumes
