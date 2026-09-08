from db import connectToDataBase,getEnv
from models import User, Delivery, UseresDeliveries
import validations as val
from questionary import select

db = connectToDataBase(getEnv())


def get_new_status():
    new_status = select("enter new status",choices=["Waiting","In Transit","Delivered","Cancelled"]).ask()
    return new_status

def get_delivery_id():
    delivery_id = int(input("enter delivery id"))
    return delivery_id


def update_delivery_status (user:User,delivery_id:int,new_status:str) -> bool:
    try:
        delivery = Delivery.get(Delivery.id == delivery_id)
        if val.check_users_delivery(user.id,delivery.id):
            delivery.status = new_status
            delivery.save()
            return True
    except:
        raise Exception ("unable to update")

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
        Delivery.delete().where((Delivery.id == delivery_id) & (Delivery.owner == user.id)).execute()
    except:
        raise Exception("couldnt delete delivery")

def get_info_to_create():
    package=False
    destination =False
    weight=False
    status = True
    while status:
        if package==False:
            Package_name = input("enter Package name: ")
            if val.check_name_package(Package_name) == False:
                continue
            else:
                package = True
        if destination ==False:
            Destination= input("enter Destination of package: ")
            if val.check_Destination(Destination) == False:
                continue
            else:
                destination=True
        if weight == False:
            Weight= input("enter Weight of package: ")
            if val.check_Weight(weight) == True:
                continue
            else:
                weight=True
        else:
            status=False
    return [Package_name,Destination,Weight]

def create_delivery(user,package,destination,weight):
    
    data = {"package_name":package,"destination":destination,"weight":weight,"owner":user}
    Delivery.create(**data)