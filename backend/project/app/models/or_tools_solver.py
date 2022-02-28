from typing import Optional

from pydantic import BaseModel
from tortoise import models
from tortoise.contrib.pydantic import pydantic_model_creator


class OrToolsSolverPayloadSchema(BaseModel):
    capacity_hours: Optional[int] = 8
    num_vehicles: Optional[int] = 10
    minutes_at_site: Optional[int] = 5


class OrToolsSolverResponseSchema(OrToolsSolverPayloadSchema):
    tsp: Optional[str]
    environment: Optional[str]
    ortools: Optional[str]
    capacity_hours: Optional[int]
    num_vehicles: Optional[int]
    minutes_at_site: Optional[int]
    solution: Optional[dict]


class OrToolsSolver(models.Model):
    capacity_hours: Optional[int] = 8
    num_vehicles: Optional[int] = 10
    minutes_at_site: Optional[int] = 5


OrToolsSolverSchema = pydantic_model_creator(OrToolsSolver)
