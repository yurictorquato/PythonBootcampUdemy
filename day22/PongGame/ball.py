from random import randint
from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.__ball()

    def __ball(self) -> None:
        self.penup()
        self.shape("circle")
        self.color("white")
        # self.shapesize(stretch_wid=1, stretch_len=1)
        self.goto(0, 0)

    def move(self) -> None:
        self.setx(self.xcor() + 1)
        self.sety(self.ycor() + 1)
