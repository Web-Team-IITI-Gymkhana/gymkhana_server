from typing import List
from uuid import UUID, uuid4

from fastapi import APIRouter, Depends, HTTPException
from server.dependencies import get_db
from sqlalchemy.orm import Session

from .models import Event
from .schemas import EventUpdate, EventSchema

router =APIRouter(prefix="/event", tags=["Event"])

@router.get("/", response_model=List[EventSchema], status_code=200)
def retrieve_all(db: Session = Depends(get_db)):
    return db.query(Event).all()


@router.get("/{id}", response_model=EventSchema, status_code=200)
def retrieve_one(id: UUID, db: Session = Depends(get_db)):
    record = db.query(Event).filter(Event.id == id).first()
    if record is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return record


@router.post("/", response_model=EventSchema, status_code=201)
def create(event: EventUpdate, db: Session = Depends(get_db)):
    db_event = Event(**event.dict(), id=uuid4())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event


@router.patch("/{id}", response_model=EventUpdate, status_code=202)
def update(event: EventUpdate, id: UUID, db: Session = Depends(get_db)):
    record = db.query(Event).get(id)
    for key, value in vars(event).items():
        print(key, value)
        setattr(record, key, value)
    db.commit()
    return event


@router.delete("/{id}", status_code=204)
def delete_by_id(id: UUID, db: Session = Depends(get_db)):
    record = db.query(Event).get(id)
    if record is None:
        raise HTTPException(status_code=404, detail="Event not found")

    db.delete(record)
    db.commit()

    return None