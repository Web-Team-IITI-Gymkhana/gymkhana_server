from server.connection import Base
from sqlalchemy import Boolean, Column, Integer, String, Text


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    email = Column(String(255), nullable=False, index=True, unique=True)
    name = Column(String(50), nullable=False)
    avatar = Column(String(255))
    user_type = Column(String(255), nullable=False)
    is_verified = Column(Boolean, nullable=False)

    def __repr__(self):
        return self.email

class Blacklisted_Token(Base):
    __tablename__ = "blacklisted_token"
    token = Column(Text, primary_key=True)
