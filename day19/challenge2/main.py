import turtle
from random import randint
from turtle import Turtle, Screen


def move_forwards(object: Turtle) -> None:
    object.forward(randint(1, 10))


def make_turtles() -> None:
    pass


def main():
    for i in range(5):
        match i:
            case 0:
                timmy = Turtle(shape="turtle")

                timmy.color("red")
            case 1:
                tommy = Turtle(shape="turtle")

                tommy.color("green")
            case 2:
                fred = Turtle(shape="turtle")

                fred.color("blue")
            case 3:
                bob = Turtle(shape="turtle")

                bob.color("yellow")
            case 4:
                clara = Turtle(shape="turtle")

                clara.color("black")
            case _:
                pass

    screen = Screen()

    screen.setup(width=500, height=500)

    bet = turtle.textinput("Make your bet", "Who will win the race? Enter a colour:")

    timmy.penup()
    timmy.goto(-250, -60)
    timmy.forward(randint(0, 20))

    tommy.penup()
    tommy.goto(-250, -30)

    fred.penup()
    fred.goto(-250, 0)

    bob.penup()
    bob.goto(-250, 30)

    clara.penup()
    clara.goto(-250, 60)

    screen.exitonclick()


if __name__ == '__main__':
    main()
