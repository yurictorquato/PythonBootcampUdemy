from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position: int):
        super().__init__()
        self.__paddle(position)

    def __paddle(self, position: int) -> None:
        self.penup()
        self.setx(position)
        self.setheading(90)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)

    def go_up(self) -> None:
        self.forward(20)

    def go_down(self) -> None:
        self.forward(-20)
