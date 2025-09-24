from day16.OOPCoffeeMachineProject.menu import MenuItem


class CoffeeMaker:
    def report(self):
        pass

    def is_resources_sufficient(self, drink: MenuItem) -> bool:
        for item in drink.ingredients:
            if drink.ingredients.values < item:
                print(f"Sorry there is not enough {}.")

                return False

        return True

    def make_coffee(self, order: MenuItem):