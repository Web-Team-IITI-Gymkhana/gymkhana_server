from authlib.integrations.starlette_client import OAuth, OAuthError
from fastapi import APIRouter, Depends, Request
from server.config import settings
from server.dependencies import get_db
from sqlalchemy.orm import Session
from starlette.config import Config
from starlette.responses import JSONResponse

from .encryption import get_current_user_token, get_token, refresh_token
from .processes import add_blacklist_token, register_or_login

router = APIRouter(prefix="/auth", tags=["Users"])


starlette_config = Config(".env")
oauth = OAuth(starlette_config)
oauth.register(
    name="google",
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={"scope": "openid email profile"},
)


@router.get("/login")
async def login_via_google(request: Request):
    redirect_uri = request.url_for("retrieve_token")
    return await oauth.google.authorize_redirect(request, redirect_uri)


@router.get("/token")
async def retrieve_token(request: Request, db: Session = Depends(get_db)):
    try:
        access_token = await oauth.google.authorize_access_token(request)
    except OAuthError:
        raise settings.invalid_credentials()
    user_data = await oauth.google.parse_id_token(request, access_token)
    user_type = "student"
    email = user_data["email"]
    user_type = register_or_login(user_data, user_type, db)
    return JSONResponse(
        {
            "result": True,
            "access_token": get_token(email, user_type, "access"),
            "refresh_token": get_token(email, user_type, "refresh"),
        }
    )


@router.post("/refresh")
async def refresh(request: Request):
    try:
        form = await request.json()
        print(form)
        if form.get("grant_type") == "refresh_token":
            token = form.get("refresh_token")
            return refresh_token(token)
    except Exception:
        raise settings.invalid_credentials()
    raise settings.invalid_credentials()


@router.get("/logout")
def logout(token: str = Depends(get_current_user_token), db: Session = Depends(get_db)):
    if add_blacklist_token({"token": token}, db=db):
        return JSONResponse({"result": True})
    raise settings.invalid_credentials()
