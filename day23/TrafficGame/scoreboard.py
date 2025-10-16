from turtle import Turtle

FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self._level = 1
        self.hideturtle()
        self.teleport(-260, 260)
        self.color("black")
        self.update_scoreboard()

    # MÉTODOS: geralmente verbos (ações)
    def update_scoreboard(self) -> None:
        self.clear()
        self.write(arg=f"Level: {self.level}", font=FONT)

    def add_level(self) -> None:
        self._level += 1
        self.update_scoreboard()

    def win_game(self) -> None:
        self.teleport(0, 0)
        self.write(arg="CONGRATULATIONS, YOU FINISH THE GAME!", align="center", font=FONT)

    def game_over(self) -> None:
        self.teleport(0, 0)
        self.write(arg="GAME OVER", align="center", font=FONT)

    # PROPERTY: geralmente substântivos (coisas)
    @property
    def level(self):
        return self._level
