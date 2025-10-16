from random import randint, choice, random
from turtle import Turtle

COLORS = ["red", "gray", "yellow", "blue", "pink", "purple", "green", "orange"]


class Car(Turtle):

    def __init__(self) -> None:
        super().__init__()

        self.shape("square")
        self.shapesize(1, 2)
        self.color(choice(COLORS))
        self.penup()
        self.teleport(randint(300, 350), randint(-230, 280))

    def move(self, speed: int) -> None:
        self.backward(speed)


class CarManager:

    def __init__(self) -> None:
        self._cars: list[Car] = []
        self._speed: int = 5

    def add_car(self) -> None:
        if random() < 0.2:
            car = Car()
            self._cars.append(car)

    def move_all_cars(self) -> None:
        """Move todos os carros com a velocidade atual."""
        for car in self._cars:
            car.move(self._speed)

    def move_faster(self) -> None:
        self._speed += 5

    @property
    def cars(self):
        return self._cars
