import logging

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.api import ping, resumes
from app.db import init_db


log = logging.getLogger("uvicorn")
# TODO log level?

def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(ping.router)
    application.include_router(resumes.router, prefix="/resumes", tags=["resumes"])

    return application


app = create_application()


@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")
    init_db(app)


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")
