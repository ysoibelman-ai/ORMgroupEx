from peewee import *
from datetime import datetime
from db import connectToDataBase, getEnv

class BaseModel(Model):
    class Meta:
        database = connectToDataBase(getEnv())

class User(BaseModel):
    id=PrimaryKeyField()
    username=CharField(unique=True,null=False)
    password_hash = CharField(unique=True)
    created_at=DateTimeField(default=datetime.now)
        
class Delivery (BaseModel):
    id = PrimaryKeyField()
    package_name = CharField(null=False)
    destination = CharField(null=False)
    weight = FloatField(constraints=[Check('weight>0')])
    status = CharField (default="Waiting")
    owner = ForeignKeyField(User, backref= "deliveries",column_name="owner_id")
    created_at = DateTimeField(default = datetime.now)

class UseresDeliveries(BaseModel):
    user_id = ForeignKeyField(User, backref= "usersdeliveries")
    delivery_id = ForeignKeyField(Delivery, backref= "usersdeliveries")