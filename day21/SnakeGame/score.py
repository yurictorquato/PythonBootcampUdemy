from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Arial", 16, "normal")


class Score(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.counter = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.update_score()


    def update_score(self) -> None:
        self.write(arg=f"Score: {self.counter}", align=ALIGNMENT, font=FONT)


    def add_counter(self) -> None:
        self.counter += 1
        self.clear()
        self.update_score()


    def game_over(self) -> None:
        self.goto(0, 0)
        self.write(arg="Game Over", align=ALIGNMENT, font=FONT)
