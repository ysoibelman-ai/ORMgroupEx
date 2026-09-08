import bcrypt
from peewee import *
from models import *


def check_password_length(password):
    if len(password)<6:
        raise Exception("Password must be at least 6 characters long")

def check_user(username):
    for user in User.select().where(User.username == username):
        if user == None:
            print("login fails! ")
            return None
        else:
            return user.username
          
def check_password(password,hashed_password):
    if bcrypt.checkpw(password, hashed_password):
        print("Authentication successful: password correct!")
    else:
        print("Authentication failed: Incorrect password!")