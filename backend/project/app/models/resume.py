from typing import Optional

from pydantic import BaseModel
from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class ResumePayloadSchema(BaseModel):
    title: str
    shortDescription: Optional[str] = ""
    name: str
    email: Optional[str] = ""
    phone: Optional[str] = ""
    public_id: str


class ResumeResponseSchema(ResumePayloadSchema):
    id: int


class Resume(models.Model):
    title = fields.TextField()
    shortDescription = fields.TextField()
    name = fields.TextField()
    email = fields.TextField()
    phone = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
    public_id = fields.CharField(unique=True, max_length=6)


ResumeSchema = pydantic_model_creator(Resume)
