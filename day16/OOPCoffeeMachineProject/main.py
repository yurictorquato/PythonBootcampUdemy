from day16.OOPCoffeeMachineProject.coffee_maker import CoffeeMaker
from day16.OOPCoffeeMachineProject.menu import Menu
from day16.OOPCoffeeMachineProject.money_machine import MoneyMachine


def main():
    money_machine = MoneyMachine()
    coffee_maker = CoffeeMaker()
    menu = Menu()

    while True:
        options = menu.get_items()
        choice = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()

        if choice == "off":
            break
        elif choice == "report":
            money_machine.report()
            coffee_maker.report()
        else:
            drink = menu.find_drink(choice)
            
            if money_machine.make_payment(drink.cost()) and money_machine.make_payment(drink.cost()):
                coffee_maker.make_coffee(drink)


if __name__ == '__main__':
    main()
