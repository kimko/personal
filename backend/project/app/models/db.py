import os
import sys

from fastapi import FastAPI
from tortoise import Tortoise, run_async
from tortoise.contrib.fastapi import register_tortoise

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


async def generate_schema() -> None:
    print("Initializing Tortoise...(GHA CI/CD)")

    await Tortoise.init(
        db_url=os.environ.get("DATABASE_URL"),
        modules={"models": ["resume"]},
    )
    print("Generating database schema via Tortoise...")
    await Tortoise.generate_schemas()
    await Tortoise.close_connections()


async def aerich_migration():
    print("Initializing Tortoise...")

    await Tortoise.init(
        db_url=os.environ.get("DATABASE_URL"),
        modules={"models": ["resume", "aerich.models"]},
    )
    print("Running aerich migrations")
    from pathlib import Path

    from aerich.models import Aerich
    from aerich.utils import get_version_content_from_file
    from resume import Resume
    from tortoise.exceptions import OperationalError
    from tortoise.transactions import in_transaction

    migrated = False
    appx = ""
    migrate_location = "./migrations/models"
    for version_file in sorted(
        filter(lambda x: x.endswith("sql"), os.listdir(migrate_location)),
        key=lambda x: int(x.split("_")[0]),
    ):
        try:
            exists = await Aerich.exists(version=version_file, app=appx)
            print(f"exists: {exists} {version_file}")
        except OperationalError:
            exists = False
        if not exists:
            async with in_transaction("default") as conn:
                file_path = Path(migrate_location, version_file)
                content = get_version_content_from_file(file_path)
                upgrade_query_list = content.get("upgrade")
                for upgrade_query in upgrade_query_list:
                    await conn.execute_script(upgrade_query)
                content = {}
                for model in [Resume]:
                    describe = model.describe()
                    content[describe.get("name")] = describe
                await Aerich.create(
                    version=version_file,
                    app=appx,
                    content=content,
                )
            print(f"Success upgrade {version_file}")
            migrated = True
    if not migrated:
        print("No upgrade items found")


if __name__ == "__main__":
    print(f"DB Comand called with {sys.argv[1:]}")
    if "migrate" in sys.argv[1:]:
        run_async(aerich_migration())
    else:
        print("Path only used by GHA CI/CD)")
        run_async(generate_schema())
