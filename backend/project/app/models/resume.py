from typing import List, Optional
from pydantic import BaseModel

from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator

class ResumePayloadSchema(BaseModel):
    title: str
    shortDescription: Optional[str] = ""
    name: str
    email: Optional[str] = ""
    phone: Optional[str] = ""

class ResumeResponseSchema(ResumePayloadSchema):
    id: int

class Resume(models.Model):
    title = fields.TextField()
    shortDescription = fields.TextField()
    name = fields.TextField()
    email = fields.TextField()
    phone = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.url

ResumeSchema = pydantic_model_creator(Resume)
