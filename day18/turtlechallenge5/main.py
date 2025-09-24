from random import randint
from turtle import Turtle, Screen, colormode


def random_color() -> tuple[int, int, int]:
    return randint(0, 255), randint(0, 255), randint(0, 255)


def make_spirograph(object: Turtle, angle: int) -> None:
    object.speed("fastest")

    for i in range(int(360 / angle)):
        object.pencolor(random_color())

        object.circle(100)
        object.left(angle)


def main():
    timmy = Turtle()
    screen = Screen()

    timmy.shape("turtle")

    colormode(255)

    make_spirograph(timmy, 5)

    screen.exitonclick()


if __name__ == '__main__':
    main()