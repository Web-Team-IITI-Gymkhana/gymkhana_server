from typing import List

from fastapi import APIRouter, Depends
from server.dependencies import get_db
from sqlalchemy.orm import Session

from .models import Hostel
from .schemas import HostelSchema

router = APIRouter(prefix="/hostel", tags=["/hostel"])


@router.get("/", response_model=List[HostelSchema], status_code=200)
def index(db: Session = Depends(get_db)):
    return db.query(Hostel).all()
