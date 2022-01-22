from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class Hostel(BaseModel):
    id: UUID
    name: str
    warden: Optional[str] = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": "7e4d6231-85ef-45e1-af1d-69e1f42b29c1",
                "name": "Devi Ahilya",
                "warden": "John Doe",
            }
        }
