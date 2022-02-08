from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import HTMLResponse

from eatery.router import router as Eatery_Router
from event.router import router as Event_Router
from hostel.router import router as Hostel_Router
from server.config import settings
from users.auth import router as Auth_Router

tags_metadata = [
    {"name": "Hostel", "description": "CRUD Operations on Hostel"},
    {"name": "Eatery", "description": "CRUD Operations on Eatery"},
    {"name": "Event", "description": "CRUD Operations on Event"},
    {"name": "Users", "description": "Google OAuth"},
]

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

ALLOWED_HOSTS = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_HOSTS,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

SECRET_KEY = settings.SECRET_KEY
if SECRET_KEY is None:
    raise "Missing SECRET_KEY"
app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)


app.include_router(Hostel_Router)
app.include_router(Eatery_Router)
app.include_router(Event_Router)
app.include_router(Auth_Router)


@app.get("/")
async def root():
    return HTMLResponse('<body><a href="/auth/login">Log In</a></body>')



# @app.get("/token")
# async def token(request: Request):
#     return HTMLResponse(
#         """
#                 <button onClick='fetch("http://127.0.0.1:8000/api/").then(
#                     (r)=>r.json()).then((msg)=>{console.log(msg)});'>
#                 Call Unprotected API
#                 </button>

#                 <button onClick='fetch("http://127.0.0.1:8000/api/protected").then(
#                     (r)=>r.json()).then((msg)=>{console.log(msg)});'>
#                 Call Protected API without JWT
#                 </button>

#                 <button onClick='fetch("http://127.0.0.1:8000/api/protected",{
#                     headers:{
#                         "Authorization": "Bearer " + window.localStorage.getItem("jwt")
#                     },
#                 }).then((r)=>r.json()).then((msg)=>{console.log(msg)});'>
#                 Call Protected API wit JWT
#                 </button>

#                 <button onClick="send()">Get FastAPI JWT Token</button>
#                 <button onClick='fetch("http://127.0.0.1:8000/logout",{
#                     headers:{
#                         "Authorization": "Bearer " + window.localStorage.getItem("jwt")
#                     },
#                 }).then((r)=>r.json()).then((msg)=>{
#                     console.log(msg);
#                     if (msg["result"] === true) {
#                         window.localStorage.removeItem("jwt");
#                     }
#                     });'>
#                 Logout
#                 </button>
#                 <button onClick='fetch("http://127.0.0.1:8000/auth/refresh",{
#                     method: "POST",
#                     headers:{
#                         "Authorization": "Bearer " + window.localStorage.getItem("jwt")
#                     },
#                     body:JSON.stringify({
#                         grant_type:\"refresh_token\",
#                         refresh_token:window.localStorage.getItem(\"refresh\")
#                         })
#                 }).then((r)=>r.json()).then((msg)=>{
#                     console.log(msg);
#                     if (msg["result"] === true) {
#                         window.localStorage.setItem("jwt", msg["access_token"]);
#                     }
#                     });'>
#                 Refresh
#                 </button>
#                 <script>
#                 function send(){
#                     var req = new XMLHttpRequest();
#                     req.onreadystatechange = function() {
#                         if (req.readyState === 4) {
#                             console.log(req.response);
#                             if (req.response["result"] === true) {
#                                 window.localStorage.setItem('jwt', req.response["access_token"]);
#                                 window.localStorage.setItem('refresh', req.response["refresh_token"]);
#                             }
#                         }
#                     }
#                     req.withCredentials = true;
#                     req.responseType = 'json';
#                     req.open("get", "/auth/token?"+window.location.search.substr(1), true);
#                     req.send("");

#                 }
#                 </script>
#             """
#     )
