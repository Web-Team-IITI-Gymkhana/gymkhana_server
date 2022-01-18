import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

database_username = os.getenv("DATABASE_USERNAME")
database_password = os.getenv("DATABASE_PASSWORD")
database = os.getenv("DATABASE")
debug = os.getenv("IN") == "development"

connection_string = (
    f"postgresql://{database_username}:{database_password}@localhost/{database}"
)

engine = create_engine(connection_string, echo=debug)

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()
