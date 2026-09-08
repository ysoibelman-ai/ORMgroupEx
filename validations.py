import bcrypt
from peewee import *
from models import *

def check_user(username):
    for user in User.select().where(User.username == username):
        if user == None:
            print("login fails! ")
            return None
        else:
            return user.username
def check_pw(password,hashed_password):
    if bcrypt.checkpw(password, hashed_password):
        print("Authentication successful: password correct!")
    else:
        print("Authentication failed: Incorrect password!")   