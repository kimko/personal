import logging
import os

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

log = logging.getLogger("uvicorn")
TORTOISE_ORM = {
    "connections": {"default": os.environ.get("DATABASE_URL")},
    "apps": {
        "models": {
            "models": ["app.models.resume", "aerich.models"],
            "default_connection": "default",
        },
    },
}
TORTOISE_ORM_TEST = {
    "connections": {"default": os.environ.get("DATABASE_TEST_URL")},
    "apps": {
        "models": {
            "models": ["app.models.resume", "aerich.models"],
            "default_connection": "default",
        },
    },
}


def init_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        db_url=os.environ.get("DATABASE_URL"),
        modules={"models": ["app.models.resume"]},
        generate_schemas=False,
        add_exception_handlers=True,
    )
