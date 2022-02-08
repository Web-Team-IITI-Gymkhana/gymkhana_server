from uuid import UUID
from typing import Literal
from pydantic import BaseModel, EmailStr, HttpUrl

class Token_Schema(BaseModel):
    token: str
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
            }
        }

class User_Schema(BaseModel):
    email: EmailStr
    name: str
    avatar: HttpUrl
    user_type: Literal["student", "body", "faculty", "staff"]
    is_verified: bool

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "email": "pclub@iiti.ac.in",
                "name": "Programming Club",
                "avatar": "https://www.vectorstock.com/royalty-free-vector/user-icon-male-person-symbol-profile-avatar-vector-20787340",
                "user_type": "body",
                "verified": True,
            }
        }

