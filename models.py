from connection import Base
from sqlalchemy import String, Integer, Column


class Hostel(Base):
    __tablename__ = 'Hostel'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)

    def __repr__(self):
        return self.name
