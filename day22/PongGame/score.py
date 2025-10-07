from turtle import Turtle


FONT = ("Arial", 70, "normal")


class Scoreboard(Turtle):

    def __init__(self, align: int) -> None:
        super().__init__()
        self.counter = 0
        self.__align = align
        self.hideturtle()
        self.penup()
        self.goto(self.__align, 190)
        self.color("white")
        self.update_score()

    def update_score(self) -> None:
        self.write(arg=self.counter, font=FONT)

    def add_counter(self) -> None:
        self.counter += 1
        self.clear()
        self.update_score()
