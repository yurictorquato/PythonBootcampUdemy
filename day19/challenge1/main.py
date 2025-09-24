from turtle import Turtle, Screen


def move_forwards(object: Turtle) -> None:
    object.forward(10)


def move_backwards(object: Turtle) -> None:
    object.backward(10)


def counter_clockwise(object: Turtle) -> None:
    object.left(10)


def clockwise(object: Turtle) -> None:
    object.right(10)


def clear_drawing(object: Turtle) -> None:
    object.clear()
    object.penup()
    object.home()
    object.pendown()
    

def main():
    timmy = Turtle()
    screen = Screen()

    screen.listen()
    screen.onkey(key="w", fun=lambda: move_forwards(timmy))
    screen.onkey(key="s", fun=lambda: move_backwards(timmy))
    screen.onkey(key="a", fun=lambda: counter_clockwise(timmy))
    screen.onkey(key="d", fun=lambda: clockwise(timmy))
    screen.onkey(key="c", fun=lambda: clear_drawing(timmy))

    screen.exitonclick()


if __name__ == '__main__':
    main()
