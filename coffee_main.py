from list import *
from coffee_machine import *

obj = Coffee()
Again = True
permit = True
while Again:
    payment = int(input("Payment: Rs "))
    choice = input("What would you like to have? (expresso,latte,cappuccino):")
    if payment >= Menu[choice]["cost"]:
        for key in Menu:
             if choice == key:
                permit = obj.resource_checker(choice)
                if not permit:
                    print("Out of resources...")
                elif permit:
                    print(f"Here is your {choice}....")
    else:
           print(f"Sorry {payment} is not enough for {choice}")

    if choice == "menu" or choice == 'm':
        print(obj.MENU())
    elif choice == "resources" or choice == 'r':
        print(obj.resources_details())
        print(f"total profit = Rs {obj.profit}")
    elif choice == "refill" or choice == 'rf':
        obj.refill()
    if choice == "off":
        exit()
