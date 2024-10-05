MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150, 
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100, 
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#  TODO: 1. Print a report of all the coffee machine resources.
#  TODO: 2. Check resources sufficient to make drink order.
money = 0
total = 0
order = "report"
def show_report():
    """Reports amount of resources remaining and money collected"""
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    print(f"Water: {water}ml\n"f"Milk: {milk}ml\n"f"Coffee: {coffee}g\n"f"Money: ${money}" )


def resources_usage():
    """Subtracts the resources used by the order"""
    resources["water"] = resources["water"] - MENU[order]["ingredients"]["water"]
    resources["coffee"] = resources["coffee"] - MENU[order]["ingredients"]["coffee"]
    if order == "espresso":
        return
    else:
        resources["milk"] = resources["milk"] - MENU[order]["ingredients"]["milk"]


def resources_check():
    """Checks to see if there's enough resources remaining to complete the order."""
    if resources["water"] < MENU[order]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
    elif resources["coffee"] < MENU[order]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee.")
    elif order == "espresso":
        return
    elif resources["milk"] < MENU[order]["ingredients"]["milk"]:
        print("Sorry there is not enough milk.")



while order != "off":
    order = input("What would you like?: (espresso/latte/cappuccino) ").lower()
    if order == "espresso" or order == "latte" or order == "cappuccino":
        resources_check()
    if order == "off":
        break
    elif order == "report":
        show_report()
        continue
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * .25
    dimes = int(input("How many dimes?: ")) * .10
    nickles = int(input("How many nickles?: ")) * .05
    pennies = int(input("How many pennies?: ")) * .01
    
    user_money = quarters + dimes + nickles + pennies

    price = MENU[order]["cost"]
    if user_money < price:
        print("Sorry that's not enough money. Money refunded.")
        continue
    total += round(user_money - price, 2)
    money += price
    resources_usage()
    print(f"Here is ${total} in change.")
    print(f"Here is your {order} Enjoy!")


# TODO if .
# purchase successful subtract coffee type resources from main resources(maybe create a function) 

