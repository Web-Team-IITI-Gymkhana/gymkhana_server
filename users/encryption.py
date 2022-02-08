from time import time
from typing import Literal

import jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from pydantic import EmailStr
from server.config import settings
from server.dependencies import get_db
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from .processes import is_token_blacklisted

if settings.API_SECRET_KEY is None:
    raise BaseException("Missing API_SECRET_KEY env var.")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


def create_token(data: dict, expires_in: int):
    issued_at = int(time())
    expires_on = issued_at + (expires_in * 60)
    json_web_token = {"iss": settings.URL, "exp": expires_on, "iat": issued_at}
    json_web_token.update(data)
    encoded_jwt = jwt.encode(
        json_web_token, settings.API_SECRET_KEY, algorithm=settings.API_ALGORITHM
    )
    return encoded_jwt


def decode_token(token):
    return jwt.decode(
        token,
        settings.API_SECRET_KEY,
        algorithms=[settings.API_ALGORITHM],
        options={"require": ["exp", "iss", "sub", "iat"]},
    )


def get_token(
    email: EmailStr,
    user_type: Literal["student", "body", "faculty", "staff"],
    token_type: Literal["access", "refresh"],
):
    if token_type == "access":
        token_expires_in = settings.ACCESS_TOKEN_EXPIRE_MINUTES
    else:
        token_expires_in = settings.REFRESH_TOKEN_EXPIRE_MINUTES
    token = create_token(
        data={"sub": email, "user_type": user_type, "typ": token_type},
        expires_in=token_expires_in,
    )
    return token


async def get_current_user_email(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    if is_token_blacklisted({"token": token}, db=db):
        raise settings.invalid_credentials()
    try:
        payload = decode_token(token)
        email: str = payload.get("sub")
        if email is None:
            raise settings.invalid_credentials()
        return email
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=401,
            detail="Token Expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except jwt.PyJWTError:
        raise settings.invalid_credentials()


async def refresh_token(token):
    try:
        payload = decode_token(token)
        email: str = payload.get("sub")
        user_type: str = payload.get("user_type")

        if email is None:
            raise settings.invalid_credentials()
        return JSONResponse(
            {"result": True, "access_token": get_token(email, user_type, "access")}
        )
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=401,
            detail="Token Expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except jwt.PyJWTError:
        raise settings.invalid_credentials()


async def get_current_user_token(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    await get_current_user_email(token, db=db)
    return token
