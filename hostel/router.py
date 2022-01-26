from typing import List
from uuid import UUID, uuid4

from fastapi import APIRouter, Depends, HTTPException, Response
from server.dependencies import get_db
from sqlalchemy.orm import Session

from .models import Hostel
from .schemas import HostelUpdate, HostelSchema

router = APIRouter(prefix="/hostel", tags=["/hostel"])


@router.get("/", response_model=List[HostelSchema], status_code=200)
def retrieve_all(db: Session = Depends(get_db)):
    return db.query(Hostel).all()


@router.get("/{id}", response_model=HostelSchema)
def retrieve_one(id: UUID, db: Session = Depends(get_db)):
    hostel = db.query(Hostel).filter(Hostel.id == id).first()
    if hostel is None:
        raise HTTPException(status_code=404, detail="Hostel not found")
    return hostel


@router.post("/", response_model=HostelSchema)
def create(hostel: HostelUpdate, db: Session = Depends(get_db)):
    db_hostel = Hostel(**hostel.dict(), id=uuid4())
    db.add(db_hostel)
    db.commit()
    return db_hostel


@router.patch("/{id}", response_model=HostelUpdate, status_code=202)
def update(hostel: HostelUpdate, db: Session = Depends(get_db)):
    pass


@router.delete("/{id}", status_code=204)
def delete_by_id(id: UUID, db: Session = Depends(get_db)):
    hostel = db.query(Hostel).get(id)
    if hostel is None:
        raise HTTPException(status_code=404, detail="Hostel not found")

    db.delete(hostel)
    db.commit()

    return None
