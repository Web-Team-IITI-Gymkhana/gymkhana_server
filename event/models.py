import datetime
from server.connection import Base
from sqlalchemy import Column, String, DateTime,Boolean
from sqlalchemy.dialects.postgresql import UUID

class Event(Base):
    __tablename__ = "event"
    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(String(2000), nullable=False)
    created_on = Column(DateTime, nullable=False,default=datetime.datetime.now)
    last_update = Column(DateTime, nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    image = Column(String(255), nullable=False)
    website = Column(String(255), nullable=True)
    notify = Column(Boolean, nullable=False)
    is_online = Column(Boolean, nullable=False)
    meet_link = Column(String(255), nullable=True)
    venue = Column(String(255), nullable=True)
    
    def __repr__(self):
        # TODO
        return self.name