# TODO: 1. Print report of all machine resources

from typing import TypedDict

class Drink(TypedDict):
    ingredients: dict[str, int]
    cost: float


MENU: dict[str, Drink] = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5
    },

    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 100,
            "coffee": 24
        },
        "cost": 2.5
    },

    "capuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0
}

profit = 0.0

def is_resources_sufficient(order_ingredients: dict[str, int]) -> bool:
    """Returns True when order can be made, False if ingredients are insufficient"""

    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")

            return False

    return True


def process_coins() -> float:
    """Returns the total calculated from coins inserted"""

    print("Please, insert coins.")

    total = int(input("How many quarters do you insert? ")) * 0.25
    total += int(input("How many dimes do you insert? ")) * 0.10
    total += int(input("How many nickles do you insert? ")) * 0.05
    total += int(input("How many pennies do you insert? ")) * 0.01

    return total


def is_transaction_successful(money_received: float, drink_cost: float) -> bool:
    """Return True when the payment is accepted, or False if money isn't enough"""

    if money_received < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        
        return False

    change = round((money_received - drink_cost), 2)
    print(f"Here is ${change} in change.")

    global profit
    profit += drink_cost

    return True


def make_coffee(drink_name: str, order_ingredients: dict[str, int]):
    """Deduct the required ingredients from the resources"""

    for item in order_ingredients:
        resources[item] -= order_ingredients[item]

    print(f"Here is your {drink_name}")


def main():
    while True:
        user_choice = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()

        if user_choice == "off":
            break

        if user_choice == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}ml")
            print(f"Money: ${profit:.2f}")

        if user_choice in ["espresso", "latte", "cappuccino"]:
            drink = MENU[user_choice]

            if is_resources_sufficient(drink["ingredients"]):
                payment = process_coins()

                if is_transaction_successful(payment, drink["cost"]):
                    make_coffee(user_choice, drink["ingredients"])


if __name__ == '__main__':
    main()
