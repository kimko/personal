import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db import init_db
from app.handlers import ping, resumes

log = logging.getLogger("uvicorn")
# TODO log level?

# TODO move this to config!
origins = [
    "https://kimko.github.io",
    # "http://localhost:3000",
]


def create_application() -> FastAPI:
    application = FastAPI()
    application.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
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
