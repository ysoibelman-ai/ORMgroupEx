from questionary import select
from auth import *
from db import connectToDataBase, getEnv
from tables import initualize_database
from deliveries import *

def run_application():
    db = connectToDataBase(getEnv())
    initualize_database(db)

    application_choice = select("===SPACE DELIVERY MANAGER===",choices = ["Register","Login","exit"]).ask()
    if application_choice == "exit":
        exit()
    elif application_choice == "Register":
        username,password=get_username_password()
        val.check_user_exists(username)
        register_user(username,password)
        login_menu(username)

    elif application_choice == "Login":
        username,password = get_username_password()
        val.check_user(username)
        login_menu(username)

def login_menu(username):
    user = User.get(User.username == username)
    login_select = select(f"WELCOME {username}", choices = ["create delivery","show my deliveries","update delivery status","delete delivery","Logout"]).ask()
    if login_select == "create delivery":
        package_name,destination,weight = get_info_to_create()
        create_delivery(user,package_name,destination,weight)
    elif login_select == "show my deliveries":
        get_user_deliveries(user)
    elif login_select == "update delivery status":
        delivery_id = get_delivery_id()
        new_status = get_new_status()
        update_delivery_status(user,delivery_id,new_status)
    elif login_select == "delete delivery":
        delivery_id = get_delivery_id()
        delete_delivery(user,delivery_id)
    elif login_select == "Logout":
        print ("Logged out successfully")
        run_application()

run_application()
