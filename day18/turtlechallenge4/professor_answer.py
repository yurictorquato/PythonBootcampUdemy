from turtle import Turtle, Screen
from random import choice


COLORS = ["red", "green", "orange", "blue", "gray", "yellow"]


def random_walk(object: Turtle, steps: int) -> None:
    directions = [0, 90, 180, 270]

    object.pensize(15)
    object.speed("slow")

    for _ in range(steps):
        object.pencolor(choice(COLORS))

        object.forward(25)
        object.setheading(choice(directions))


def main():
    timmy = Turtle()
    screen = Screen()

    timmy.shape("turtle")

    random_walk(timmy, 100)

    screen.exitonclick()


if __name__ == '__main__':
    main()
