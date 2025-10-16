from turtle import Turtle


class Player(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.initial_position()

    def move_up(self) -> None:
        self.forward(10)

    def move_down(self) -> None:
        self.forward(-10)

    def initial_position(self) -> None:
        self.teleport(0, -280)

    def is_at_finish_line(self) -> bool:
        if self.ycor() < 280:
            return False

        return True
