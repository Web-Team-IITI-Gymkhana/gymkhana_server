from Server.config import settings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

debug = settings.DEBUG
connection_string = settings.CONNECTION_STRING

engine = create_engine(connection_string, echo=debug)

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()
