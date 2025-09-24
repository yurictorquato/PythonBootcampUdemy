from turtle import Turtle, Screen


def draw_square(object: Turtle, size: int | float) -> None:
    """Cria um quadrado"""
    for _ in range(4):
        object.forward(size)
        object.right(90)


def main():
    timmy = Turtle()
    screen = Screen()

    timmy.shape("turtle")
    timmy.color("green")

    draw_square(timmy, 250)

    for i in range(4):
        if i < 3:
            timmy.forward(100)
            timmy.right(90)
        else:
            timmy.forward(100)

    screen.exitonclick()


if __name__ == '__main__':
    main()
