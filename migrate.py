# Migration File 
# needs to be ran once while setting up the server
from connection import Base, engine

Base.metadata.create_all(engine)