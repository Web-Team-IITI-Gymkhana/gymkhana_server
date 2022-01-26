from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class HostelSchema(BaseModel):
    id: UUID
    name: str
    description: str 

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": "7e4d6231-85ef-45e1-af1d-69e1f42b29c1",
                "name": "Devi Ahilya",
                "description": "To be added"
            }
        }
