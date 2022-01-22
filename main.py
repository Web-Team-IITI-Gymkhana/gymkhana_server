from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

import models
from config import settings
from connection import session

# from starlette.config import Config
# from authlib.integrations.starlette_client import OAuth

app = FastAPI(
    title=settings.TITLE,
    version=settings.VERSION,
    description=settings.DESCRIPTION,
)

# config_data = {
#     "GOOGLE_CLIENT_ID": settings.GOOGLE_CLIENT_ID,
#     "GOOGLE_CLIENT_SECRET": settings.GOOGLE_CLIENT_SECRET,
# }
# starlette_config = Config(environ=config_data)
# oauth = OAuth(starlette_config)
# oauth.register(
#     name="google",
#     server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
#     client_kwargs={"scope": "openid email profile"},
# )

# This will move to schemas.py
class Hostel(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


@app.get("/", response_model=List[Hostel], status_code=200)
def index():
    return session.query(models.Hostel).all()
