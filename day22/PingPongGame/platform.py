from turtle import Turtle


class Platform(Turtle):

    def __init__(self):
        super().__init__()
        self.paddle()

    def paddle(self) -> None:
        self.penup()
        self.setx(350)
        self.setheading(90)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=4)

    def up(self) -> None:
        self.forward(20)

    def down(self) -> None:
        # if self.position() > 300 or self.position() < -300:
        #     pass

        self.forward(-20)
