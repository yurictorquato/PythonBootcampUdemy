from turtle import Turtle, Screen
from random import choice


def make_draw(object: Turtle) -> None:
    for i in range(3, 11):
        draw_shape(object, i)


def draw_shape(object: Turtle, sides: int) -> None:
    angle = 360 / sides

    object.pencolor(choice(["red", "green", "orange", "blue", "gray", "yellow"]))

    for _ in range(sides):
        object.forward(100)
        object.right(angle)


def main():
    timmy = Turtle()
    screen = Screen()

    # for i in range(3, 11):
    #     draw_shape(timmy, i)

    make_draw(timmy)

    screen.exitonclick()


if __name__ == '__main__':
    main()
