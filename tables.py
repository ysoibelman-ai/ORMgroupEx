from db import connectToDataBase, getEnv
from models import User, Delivery, UseresDeliveries
db = connectToDataBase(getEnv())
def initualize_database():
    db.connect(reuse_if_open = True)
    db.create_tables([User,Delivery,UseresDeliveries])

