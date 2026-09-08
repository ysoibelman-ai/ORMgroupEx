from db import connectToDataBase, getEnv
from models import User, Delivery, UseresDeliveries
def initualize_database(db):
    db.connect(reuse_if_open = True)
    db.create_tables([User,Delivery,UseresDeliveries])

