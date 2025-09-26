from random import randint
from turtle import Turtle


class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.refresh()


    def refresh(self) -> None:
        self.goto(randint(-280, 280), randint(-280, 280))
