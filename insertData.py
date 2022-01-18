from models import Hostel
from connection import session

hostel = Hostel(name="Devi Ahilya")
session.add(hostel)
session.commit()
