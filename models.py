from peewee import *
from datetime import datetime
from db import db

class BaseModel(Model):
    class Meta:
        database = db