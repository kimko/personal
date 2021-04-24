from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class ResumePayloadSchema(BaseModel):
    title: str
    shortDescription: Optional[str] = ""
    name: str
    email: Optional[str] = ""
    phone: Optional[str] = ""

class ResumeResponseSchema(ResumePayloadSchema):
    id: int
