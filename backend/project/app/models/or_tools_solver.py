from typing import Optional

from pydantic import BaseModel
from tortoise import models
from tortoise.contrib.pydantic import pydantic_model_creator


class OrToolsSolverPayloadSchema(BaseModel):
    capacity_hours: Optional[int] = 8
    num_vehicles: Optional[int] = 10
    minutes_at_site: Optional[int] = 5
    duration_matrix: Optional[list] = [[0, 1556, 1884], [1572, 0, 966], [1927, 922, 0]]


class OrToolsSolverResponseSchema(BaseModel):
    solution: Optional[dict] = {
        "0": {
            "stops": [0, 166, 40],
            "duration_minutes": 5 + 171 + 45,
        },
        "1": {
            "stops": [
                0,
                128,
                32,
            ],
            "duration_minutes": 5 + 133 + 37,
        },
    }


class OrToolsSolver(models.Model):
    capacity_hours: Optional[int] = 8
    num_vehicles: Optional[int] = 10
    minutes_at_site: Optional[int] = 5


OrToolsSolverSchema = pydantic_model_creator(OrToolsSolver)
