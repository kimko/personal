from app.models.pydantic import ResumePayloadSchema
from app.models.tortoise import Resume


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
