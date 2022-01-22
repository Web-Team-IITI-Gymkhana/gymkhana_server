from typing import List

from Hostel.models import Hostel
from fastapi import FastAPI
from Hostel.schemas import HostelSchema

from Server.config import settings
from Server.connection import session

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


@app.get("/", response_model=List[HostelSchema], status_code=200)
def index():
    return session.query(Hostel).all()
