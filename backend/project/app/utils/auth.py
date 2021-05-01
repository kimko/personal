from fastapi import Depends, Header, HTTPException

from app.config import Settings, get_settings

# TODO improve security using fastapi.security


async def verify_token(
    x_token: str = Header(...), settings: Settings = Depends(get_settings)
):
    if x_token != settings.token:
        raise HTTPException(status_code=401, detail="X-Token header invalid")
