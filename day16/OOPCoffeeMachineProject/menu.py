class MenuItem:
    def __init__(self):
        self.__name = None
        self.__cost = None
        self.__ingredients = {}

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def cost(self) -> float:
        return self.__cost

    @cost.setter
    def cost(self, cost: float) -> None:
        self.__cost = cost

    @property
    def ingredients(self) -> dict[str, int]:
        return self.__ingredients

    @ingredients.setter
    def ingredients(self, value: dict[str, int]) -> None:
        self.__ingredients = value

    def __str__(self) -> str:
        return f"{self.name}"


class Menu(MenuItem):
    def get_items(self) -> str:
        pass

    def find_drink(self, order_name: str) -> None:
        pass
        
