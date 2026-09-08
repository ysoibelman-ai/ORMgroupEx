from db import connectToDataBase
from models import User, Delivery, UseresDeliveries
import validations as val
db = connectToDataBase()

def update_delivery_status (user:User,delivery_id:int,new_status:str) -> bool:
    try:
        delivery = Delivery.get(Delivery.id == delivery_id)
        if val.check_users_delivery(user.id,delivery.id):
            delivery.status = new_status
            delivery.save()
            return True
    except:
        return False

def get_user_deliveries(user:User) -> list[Delivery]:
    my_deliveries = []
    for delivery in Delivery:
        if delivery.owner == user.id:
            my_deliveries.append(delivery)
    display_user_deliveries(my_deliveries)

def display_user_deliveries(deliveries:list[Delivery]):
    if deliveries == []:
        print("You Don't Have Any Deliveries")
    else:
        for delivery in deliveries:
            print(f"ID: {delivery.id}\nPackage: {delivery.package_name}\nDestination: {delivery.destination}\nWeight: {delivery.weight}\nStatus: {delivery.status}")

def delete_delivery(user:User,delivery_id:int) -> bool:
    try:
        delivery = Delivery.get(Delivery.id == delivery_id)
        if delivery.owner == user.id:
            delivery.delete_instance()
        else:
            return False
    except:
        raise Exception("couldnt delete delivery")

    

