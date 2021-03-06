from server.connection import Base
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID


class Hostel(Base):
    __tablename__ = "hostel"
    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)

    def __repr__(self):
        return self.name
