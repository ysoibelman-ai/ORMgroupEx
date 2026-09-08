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
        

