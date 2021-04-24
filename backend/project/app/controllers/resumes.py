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
