from turtle import Turtle, Screen
from random import choice


def main():
    timmy = Turtle()
    screen = Screen()

    timmy.shape("turtle")

    for _ in range(15):
        timmy.pencolor(choice(["red", "green", "blue", "purple"]))
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
        timmy.pendown()

    screen.exitonclick()


if __name__ == '__main__':
    main()
