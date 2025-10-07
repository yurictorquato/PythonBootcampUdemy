from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self) -> None:
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    def bounce_y(self) -> None:
        self.y_move *= -1

    def bounce_x(self) -> None:
        self.x_move *= -1
        self.move_speed *= 0.5

    def reset_position(self) -> None:
        self.teleport(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
