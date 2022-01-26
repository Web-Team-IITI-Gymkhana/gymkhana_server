from authlib.integrations.starlette_client import OAuth
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.config import Config

from hostel.router import router as Hostelrouter
from server.config import settings

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

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(Hostelrouter)

config_data = {
    "GOOGLE_CLIENT_ID": settings.GOOGLE_CLIENT_ID,
    "GOOGLE_CLIENT_SECRET": settings.GOOGLE_CLIENT_SECRET,
}
starlette_config = Config(environ=config_data)
oauth = OAuth(starlette_config)
oauth.register(
    name="google",
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={"scope": "openid email profile"},
)

from starlette.middleware.sessions import SessionMiddleware

SECRET_KEY = settings.SECRET_KEY or None
if SECRET_KEY is None:
    raise "Missing SECRET_KEY"
app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)

from authlib.integrations.starlette_client import OAuthError
from fastapi import Request
from starlette.responses import RedirectResponse


@app.route("/login")
async def login(request: Request):
    redirect_uri = request.url_for("auth")
    return await oauth.google.authorize_redirect(request, redirect_uri)


@app.route("/auth")
async def auth(request: Request):
    try:
        access_token = await oauth.google.authorize_access_token(request)
    except OAuthError:
        return RedirectResponse(url="/")
    user_data = await oauth.google.parse_id_token(request, access_token)
    request.session["user"] = dict(user_data)
    return RedirectResponse(url="/")


from starlette.responses import HTMLResponse


@app.get("/")
def public(request: Request):
    user = request.session.get("user")
    if user:
        name = user.get("name")
        return HTMLResponse(f"<p>Hello {name}!</p><a href=/logout>Logout</a>")
    return HTMLResponse("<a href=/login>Login</a>")


@app.route("/logout")
async def logout(request: Request):
    request.session.pop("user", None)
    return RedirectResponse(url="/")
