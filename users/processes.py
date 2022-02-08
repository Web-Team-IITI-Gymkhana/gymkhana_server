from fastapi import Depends
from server.dependencies import get_db
from sqlalchemy.orm import Session

from users.schemas import Token_Schema
from .models import User, Blacklisted_Token


def register_or_login(user_data: dict, user_type: str, db: Session = Depends(get_db)):
    email = user_data["email"]
    name = user_data["name"]
    avatar = user_data["picture"]
    is_verified = user_data["hd"] == "iiti.ac.in"
    user = db.query(User).filter(User.email == user_data["email"]).first()
    if user is None:
        new_user = User(
            email=email,
            name=name,
            avatar=avatar,
            user_type=user_type,
            is_verified=is_verified,
        )
        db.add(new_user)
        db.commit()
        return user_type
    return user.user_type


def add_blacklist_token(token: Token_Schema, db: Session = Depends(get_db)) -> bool:
    try:
        blacklist_token = Blacklisted_Token(**token.dict())
        db.add(blacklist_token)
        db.commit()
        return True
    except:
        return False


def is_token_blacklisted(token: Token_Schema, db: Session = Depends(get_db)) -> bool:
    blacklist_token = (
        db.query(Blacklisted_Token).filter(Blacklisted_Token.token == token).first()
    )
    if blacklist_token is None:
        return False
    return True

