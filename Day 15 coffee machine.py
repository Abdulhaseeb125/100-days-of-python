MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 150,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 400,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 350,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
coins ={
    "peny" : 50,
    "rupee" : 100
}


profit = 0


def reports():
    for item in resources:
        print(f"{item} = {resources[item]}ml")


def price_details():
    for i in MENU:
        print(f'{i} : Rs {MENU[i]["cost"]}')


def coffee_menu():
    for i in MENU:
        print(f"{i}", end=", ")


def peny_counter():
    peny = int(input("enter number of peny coins:"))
    rupee = int(input("enter number of rupee coins:"))
    total = coins["peny"] * peny + coins["rupee"] * rupee
    return total


Again = True
while Again:
    choice = input(" Choose and option: Coffee"
                   " , Reports , Price_Details ").lower()
    if choice == "price_details" or choice == '3':
        price_details()
    if choice == "reports" or choice == '2':
        reports()
    if choice == "coffee" or choice == '1':
        coffee_menu()
        select = input("Your Order:")
        for i in MENU:
            if select == i:
                total = peny_counter()
                if total > MENU[i]["cost"]:
                    change = total - MENU[i]["cost"]
                    profit += total - change
                    print(f"Enjoy the coffee! here is your change: Rs {change}")
                    print(f"profit is:Rs {profit}")
                if total == MENU[i]["cost"]:
                    print(f"Enjoy the coffee!")
                    profit += total
                    print(f"profit is:Rs {profit}")
                if total < MENU[i]["cost"]:
                    print("This money is not enough..")
                    print(f"profit is:Rs {profit}")

    _ = input("Do you want to run order again:").lower()
    if _ == "n":
        Again = False
