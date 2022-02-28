import logging
from typing import Dict

from app.models.or_tools_solver import OrToolsSolverPayloadSchema

log = logging.getLogger("uvicorn")


async def solve_TSP(payload: OrToolsSolverPayloadSchema) -> Dict:
    response = {
        "tsp": "tsp",
        "environment": "dev",
        "ortools": "9.2.9972",
        "capacity_hours": 14,
        "num_vehicles": 25,
        "minutes_at_site": 5,
        "solution": {
            "0": {
                "stops": [
                    0,
                    166,
                    40,
                    41,
                    290,
                    276,
                    308,
                    302,
                    15,
                    320,
                    316,
                    307,
                    251,
                    268,
                    287,
                    242,
                    263,
                    264,
                    259,
                    247,
                    248,
                    249,
                    236,
                    240,
                    261,
                    273,
                    241,
                    252,
                    265,
                    30,
                    36,
                    27,
                    24,
                    33,
                    0,
                ],
                "duration_minutes": 658,
            },
            "1": {
                "stops": [
                    0,
                    128,
                    32,
                    77,
                    72,
                    70,
                    71,
                    66,
                    68,
                    64,
                    75,
                    62,
                    299,
                    317,
                    74,
                    277,
                    286,
                    310,
                    283,
                    274,
                    309,
                    279,
                    322,
                    225,
                    45,
                    110,
                    288,
                    142,
                    122,
                    121,
                    108,
                    107,
                    141,
                    0,
                ],
                "duration_minutes": 663,
            },
        },
    }

    return response