from typing import List

from fastapi import FastAPI, status
from pydantic import BaseModel

import models
from connection import session

app = FastAPI()


class Hostel(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


@app.get("/", response_model=List[Hostel], status_code=200)
def index():
    return session.query(models.Hostel).all()
