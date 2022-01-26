from server.connection import Base
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.dialects.postgresql import UUID


class Eatery(Base):
    __tablename__ = "eatery"
    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String(50), nullable=False)
    day = Column(Integer, nullable=False)
    breakfast = Column(Text, nullable=False)
    lunch = Column(Text, nullable=False)
    snacks = Column(Text, nullable=False)
    dinner = Column(Text, nullable=False)

    def __repr__(self):
        # TODO
        return self.name
