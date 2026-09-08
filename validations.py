import bcrypt
from peewee import *
from models import *
from deliveries import *

def check_password_length(password):
    if len(password)<6:
        raise Exception("Password must be at least 6 characters long")

def check_user_exists(username):
    for user in User.select():
        if user.username == username:
            raise Exception("username already in use")

def check_user(username):
    for user in User.select().where(User.username == username):
        if user == None:
            raise Exception ("login fails!")
          
def check_password(password,hashed_password):
    if bcrypt.checkpw(password, hashed_password):
        print("Authentication successful: password correct!")
    else:
        print("Authentication failed: Incorrect password!")
        exit()

def check_users_delivery(user_id,delivery_id) -> bool:
    for line in UseresDeliveries:
        if line.user_id == user_id and line.delivery_id == delivery_id:
            return True
        else:
            return False

def check_name_package(name_package):
    if name_package == "":
        return False
    else:
        return True
def check_Destination(Destination):
    if Destination == "":
        return False
    else:
        return True    
def check_Weight(Weight):
    if Weight >0:
        return True
    else:
        return False