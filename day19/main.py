from turtle import Turtle, Screen


def move_forwards(object: Turtle) -> None:
    object.forward(10)


def main():
    timmy = Turtle()
    screen = Screen()

    screen.listen()
    screen.onkey(key="space", fun=lambda: move_forwards(timmy))
    screen.exitonclick()


if __name__ == '__main__':
    main()
    