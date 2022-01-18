from connection import session
from models import Hostel

hostels = session.query(Hostel)
for hostel in hostels:
    print(hostel.name)
