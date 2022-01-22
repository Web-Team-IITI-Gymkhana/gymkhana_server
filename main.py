from typing import List

from fastapi import FastAPI, Depends

from Hostel import models, schemas
from Server.config import settings
from Server.connection import SessionLocal
from sqlalchemy.orm import Session

# from starlette.config import Config
# from authlib.integrations.starlette_client import OAuth

tags_metadata = [{"name": "Hostel", "description": "Basic Hostel Operations"}]

app = FastAPI(
    title=settings.TITLE,
    version=settings.VERSION,
    description=settings.DESCRIPTION,
    contact={
        "name": settings.NAME,
        "url": settings.URL,
        "email": settings.EMAIL,
    },
    license_info={
        "name": settings.LICENSE_NAME,
        "url": settings.LICENSE_URL,
    },
    openapi_tags=tags_metadata,
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


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


@app.get("/", response_model=List[schemas.Hostel], status_code=200, tags=["Hostel"])
def index(db: Session = Depends(get_db)):
    return db.query(models.Hostel).all()
