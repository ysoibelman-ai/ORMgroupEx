from peewee import *
from datetime import datetime
from db import db

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    id=PrimaryKeyField()
    username=CharField(unique=True,null=False)
    password_hash = CharField(unique=True)
    created_at=DateTimeField(default=datetime.datetime.now)
        

class Delivery (BaseModel):
    id = PrimaryKeyField()
    package_name = CharField(required = True)
    destination = CharField(required = True)
    weight = FloatField(constraints=Check('weight>0'))
    status = CharField (default="Waiting")
    owner = ForeignKeyField(User, backref= "deliveries",column_name="owner_id")
    created_at = DateTimeField(default = datetime.datetime.now)

class UseresDeliveries(BaseModel):
    user_id = ForeignKeyField(user, backref= "usersdeliveries")
    delivery_id = ForeignKeyField(delivery, backref= "usersdeliveries")



