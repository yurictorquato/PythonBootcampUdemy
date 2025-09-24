from turtle import Turtle, Screen, colormode
from random import choice, randint


def random_color() -> tuple[int, int , int]:
    return randint(0, 255), randint(0, 255), randint(0, 255)


def random_walk(object: Turtle, steps: int) -> None:
    directions = [0, 90, 180, 270]

    object.pensize(15)
    object.speed("slow")

    for _ in range(steps):
        # colors = (randint(0, 255), randint(0, 255), randint(0, 255))
        # r = randint(0, 255)
        # g = randint(0, 255)
        # b = randint(0, 255)

        # object.pencolor(colors)
        # object.pencolor(r, g, b)
        object.pencolor(random_color())

        object.forward(25)
        object.setheading(choice(directions))


def main():
    timmy = Turtle()
    screen = Screen()

    colormode(255)

    timmy.shape("turtle")

    random_walk(timmy, 100)

    screen.exitonclick()


if __name__ == '__main__':
    main()
