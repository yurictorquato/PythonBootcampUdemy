from turtle import Turtle


class Line(Turtle):

    def __init__(self):
        super().__init__()
        self.line()

    def line(self) -> None:
        self.hideturtle()
        self.penup()
        self.pensize(8)
        self.pencolor("white")
        self.sety(-400)
        self.setheading(90)

        for _ in range(20):
            self.pendown()
            self.forward(30)
            self.penup()
            self.forward(30)
