from uuid import UUID

from pydantic import BaseModel


class EateryUpdate(BaseModel):
    name: str
    day: int
    breakfast: str
    lunch: str
    snacks: str
    dinner: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "Grand Kitchen",
                "day": 0,
                "breakfast": "Poha and Milk",
                "lunch": "Sabzi Kachori and Shahi Paneer",
                "snacks": "Tea Pakoda",
                "dinner": "Dal Makhani and Aloo Naan",
            }
        }


class EaterySchema(EateryUpdate):
    id: UUID

    class Config:
        schema_extra = {
            "example": {
                "id": "7e4d6231-85ef-45e1-af1d-69e1f42b29c1",
                "name": "Grand Kitchen",
                "day": 0,
                "breakfast": "Poha and Milk",
                "lunch": "Sabzi Kachori and Shahi Paneer",
                "Snacks": "Tea Pakoda",
                "Dinner": "Dal Makhani and Aloo Naan",
            }
        }
