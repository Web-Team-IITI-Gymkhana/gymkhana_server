from typing import List
from uuid import UUID, uuid4

from fastapi import APIRouter, Depends, HTTPException
from server.dependencies import get_db
from sqlalchemy.orm import Session

from .models import Eatery
from .schemas import EateryUpdate, EaterySchema

router = APIRouter(prefix="/eatery", tags=["Eatery"])


@router.get("/", response_model=List[EaterySchema], status_code=200)
def retrieve_all(db: Session = Depends(get_db)):
    return db.query(Eatery).all()


@router.get("/{id}", response_model=EaterySchema, status_code=200)
def retrieve_one(id: UUID, db: Session = Depends(get_db)):
    record = db.query(Eatery).filter(Eatery.id == id).first()
    if record is None:
        raise HTTPException(status_code=404, detail="Eatery not found")
    return record


@router.post("/", response_model=EaterySchema, status_code=201)
def create(eatery: EateryUpdate, db: Session = Depends(get_db)):
    db_eatery = Eatery(**eatery.dict(), id=uuid4())
    db.add(db_eatery)
    db.commit()
    db.refresh(db_eatery)
    return db_eatery


@router.patch("/{id}", response_model=EateryUpdate, status_code=202)
def update(eatery: EateryUpdate, id: UUID, db: Session = Depends(get_db)):
    record = db.query(Eatery).get(id)
    for key, value in vars(eatery).items():
        print(key, value)
        setattr(record, key, value)
    db.commit()
    return eatery


@router.delete("/{id}", status_code=204)
def delete_by_id(id: UUID, db: Session = Depends(get_db)):
    record = db.query(Eatery).get(id)
    if record is None:
        raise HTTPException(status_code=404, detail="Eatery not found")

    db.delete(record)
    db.commit()

    return None
