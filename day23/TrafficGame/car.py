from random import randint, choice
from turtle import Turtle

COLORS = ["red", "gray", "yellow", "blue", "pink", "purple", "green", "orange"]


class Car(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.__speed = 10
        self.shape("square")
        self.shapesize(1, 2)
        self.color(choice(COLORS))
        self.penup()
        self.teleport(randint(300, 350), randint(-230, 280))

    def move(self) -> None:
        self.backward(self.__speed)

    def move_faster(self) -> None:
        self.__speed += 10
