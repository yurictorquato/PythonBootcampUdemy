from turtle import Turtle


class Score(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.color("white")
        self.counter = 0

    
    def add_counter(self) -> None:
        self.counter += 1
        self.clear()
        self.write(arg=f"Score: {self.counter}", align="center", font=("Arial", 16, "normal"))
        