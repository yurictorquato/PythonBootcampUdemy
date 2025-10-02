from turtle import Turtle


class Platform(Turtle):

    def __init__(self, position: int):
        super().__init__()
        self.paddle(position)

    def paddle(self, position: int) -> None:
        self.penup()
        self.setx(position)
        self.setheading(90)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)

    def up(self) -> None:
        self.forward(20)

    def down(self) -> None:
        # if self.position() > 300 or self.position() < -300:
        #     pass

        self.forward(-20)
