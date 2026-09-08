from db import connectToDataBase
from models import User, Delivery, UseresDeliveries
db = connectToDataBase()
def initualize_database():
    db.connect(reuse_if_open = True)
    db.create_tables([User,Delivery,UseresDeliveries])

