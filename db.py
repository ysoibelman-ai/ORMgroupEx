import os
from dotenv import load_dotenv
from peewee import MySQLDatabase

def getEnv ():
    load_dotenv() 
    db_name = os.getenv("DB_NAME")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD", "")
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
        
    if not all([db_name,db_user,db_host,db_port]):
        raise ValueError("Database configuration is missing")
    return [db_name,db_user,db_password,db_host,int(db_port)]


def connectToDataBase(db_info):   
    db = MySQLDatabase(
    db_info[0],
    user=db_info[1],
    password=db_info[2],
    host=db_info[3],
    port=db_info[4]
    )
    return db


