from typing import Optional
from pydantic import BaseModel
from uuid import UUID

class HostelSchema(BaseModel):
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
