from turtle import Turtle, Screen
import random


def random_walk(object: Turtle) -> None:
    # angle = int(random.random() * 360)
    angle = int(random.choice([0, 1, 2, 3]) * 90)

    object.pencolor(random.choice(["red", "green", "orange", "blue", "gray", "yellow"]))
    object.pensize(15)

    object.speed("slow")
    object.forward(25)
    object.right(angle)


def main():
    timmy = Turtle()
    screen = Screen()

    timmy.shape("turtle")

    for _ in range(100):
        random_walk(timmy)

    screen.exitonclick()


if __name__ == '__main__':
    main()
