from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Hostel(BaseModel):
    id: int
    name: str
    

@app.get("/")
def index():
    return {"name": "John Doe"}
