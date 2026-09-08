import bcrypt
from db import connectToDataBase, getEnv
from models import UseresDeliveries,User,Delivery
import validations as val

def get_username_password():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    val.check_password_length(password)
    hashed_password = hash_password(password)
    val.check_password(password.encode('utf-8'),hashed_password)
    return [username, hashed_password]

def hash_password(password):
    password = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password,salt)
    return hashed_password

def register_user(username,password):
        try:
            new_user = User.create(username = username, password_hash = password)
            return new_user
        except Exception as e:
            raise Exception("Unable to register to database") from e