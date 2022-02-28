import logging

from fastapi import APIRouter, Depends

from app.controllers import or_tools_solvers
from app.models.or_tools_solver import (
    OrToolsSolverPayloadSchema,
    OrToolsSolverResponseSchema,
)
from app.utils.auth import verify_token

router = APIRouter()
log = logging.getLogger("uvicorn")


@router.post(
    "/",
    response_model=OrToolsSolverResponseSchema,
    status_code=201,
    dependencies=[Depends(verify_token)],
)
async def solve_TSP(payload: OrToolsSolverPayloadSchema) -> OrToolsSolverResponseSchema:
    response_object = await or_tools_solvers.solve_TSP(payload)

    return response_object
