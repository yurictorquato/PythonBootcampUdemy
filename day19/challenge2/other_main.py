from random import randint
from turtle import Turtle, Screen, textinput


def make_turtles() -> list[Turtle]:
    """Make 5 turtles with different colors"""

    y = -60

    colors = ["green", "blue", "purple", "yellow", "red"]
    turtles = []

    for color in colors:
        turtle = Turtle(shape="turtle")
        turtle.color(color)
        turtle.penup()
        turtle.goto(-250, y)

        y += 30

        turtles.append(turtle)

    return turtles


def race(turtles: list[Turtle]) -> str:
    """Run the race between the given turtles"""

    arrival = 230

    while True:
        for turtle in turtles:
            turtle.forward(randint(1, 10))

            if turtle.xcor() >= arrival:
                return turtle.pencolor()



def main():
    screen = Screen()
    screen.setup(width=520, height=500)

    bet = textinput("Make your bet", "Who will win the race? Enter a colour:").strip().lower()

    turtles = make_turtles()
    winner = race(turtles)

    if bet == winner:
        print(f"You've won! The {winner} turtle is the winner!")
    else:
        print(f"You've lost! The {winner} turtle is the winner!")

    screen.exitonclick()


if __name__ == '__main__':
    main()
