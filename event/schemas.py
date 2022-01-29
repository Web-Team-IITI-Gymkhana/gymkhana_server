from uuid import UUID
from datetime import datetime
from pydantic import BaseModel
from typing import (Optional)
class EventUpdate(BaseModel):
    name: str
    description: str
    created_on: datetime
    last_update: datetime
    start_time: datetime
    end_time: datetime
    image: str
    website: str
    notify: bool
    is_online: bool
    meet_link: str
    venue: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "Winter of CP",
                "description": "It is a coding event held in the month of Decemeber by the Programming Club",
                "created_on": "2022-01-28T21:33:50.795775",
                "last_update": "2021-01-28T12:33:52.795775",
                "start_time": "2022-02-19T19:33:10.895775",
                "end_time": "2022-02-19T21:00:10.895775",
                "image": "https://www.google.com/search?",
                "website": "",
                "notify": True,
                "is_online": False,
                "meet_link": "",
                "venue": "Carbon Building",
            }
        }


class EventSchema(EventUpdate):
    id: UUID

    class Config:
        schema_extra = {
            "example": {
                "id": "f031e2a7-4d65-4b99-b57f-ce1474d1ace6",
                "name": "Winter of CP",
                "description": "It is a coding event held in the month of Decemeber by the Programming Club",
                "created_on": "2022-01-28T21:33:50.795775",
                "last_update": "2021-01-28T12:33:52.795775",
                "start_time": "2022-02-19T19:33:10.895775",
                "end_time": "2022-02-19T21:00:10.895775",
                "image": "https://www.google.com/search?",
                "website": "",
                "notify": True,
                "is_online": False,
                "meet_link": "",
                "venue": "Carbon Building",
            }
        }
