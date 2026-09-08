import bycrypt
from db import connectToDataBase, getEnv
from models import UseresDeliveries,User,Delivery

db = connectToDataBase(getEnv())
def get_username_password():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    return username, password

def hash_password(password):
    password = password.encode('utf-8')
    salt = bycrypt.gensalt()
    hashed_password = bycrypt.hashpw(password,salt)
    return hashed_password

def register_user(username,password):
    with db.connection_context(reuse_if_open=True):
        try:
            new_user = User.create(username = username, password_hash = password)
            return new_user
        except Exception as e:
            raise Exception("Unable to register to database") from e