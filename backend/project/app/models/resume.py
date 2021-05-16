from typing import Optional

from pydantic import BaseModel, Field
from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class ResumePayloadSchema(BaseModel):
    title: str
    short_description: Optional[str] = ""
    name: str
    email: Optional[str] = ""
    phone: Optional[str] = ""
    public_id: str = Field(max_length=6)
    summary: Optional[list] = []
    jobs: Optional[list] = []  # TODO schema validation


class GenerateRandomPayloadSchema(BaseModel):
    public_id: str = Field(max_length=6)


class ResumeResponseSchema(ResumePayloadSchema):
    id: int


class Resume(models.Model):
    title = fields.TextField()
    short_description = fields.TextField()
    name = fields.TextField()
    email = fields.TextField()
    phone = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
    public_id = fields.CharField(unique=True, max_length=6)
    summary = fields.JSONField()
    jobs = fields.JSONField()


ResumeSchema = pydantic_model_creator(Resume)
