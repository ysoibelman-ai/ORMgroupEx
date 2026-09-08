# from models import*
from validations import *

def get_info_to_create():
    package=False
    destination =False
    weight=False
    status = True
    while status:
        if package==False:
            Package_name = input("enter Package name: ")
            if check_name_package(Package_name) == False:
                continue
            else:
                package = True
        if destination ==False:
            Destination= input("enter Destination of package: ")
            if check_Destination(Destination) == False:
                continue
            else:
                destination=True
        if weight == False:
            Weight= input("enter Weight of package: ")
            if check_Weight(weight) == False:
                continue
            else:
                weight=True
        else:
            status=False
    return Package_name,Destination,Weight

print(get_info_to_create())



def create_delivery(user,package,destination,weight):
    data = {"package_name":package,"destination":destination,"weight":weight,"owner":user}
    Delivery.create(data)