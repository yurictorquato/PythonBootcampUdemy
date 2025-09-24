from random import choice
from turtle import Turtle, Screen

def make_geometric_figures(object: Turtle) -> None:
    for i in range(3, 11):
        match i:
            case 3:
                object.pencolor(
                    choice(["red", "green", "orange", "blue", "gray", "yellow"])
                )

                for _ in range(3):
                    object.forward(100)
                    object.right(120)
            case 4:
                object.pencolor(
                    choice(["red", "green", "orange", "blue", "gray", "yellow"])
                )

                for _ in range(4):
                    object.forward(100)
                    object.right(90)
            case 5:
                object.pencolor(
                    choice(["red", "green", "orange", "blue", "gray", "yellow"])
                )

                for _ in range(5):
                    object.forward(100)
                    object.right(72)
            case 6:
                object.pencolor(
                    choice(["red", "green", "orange", "blue", "gray", "yellow"])
                )

                for _ in range(6):
                    object.forward(100)
                    object.right(60)
            case 7:
                object.pencolor(
                    choice(["red", "green", "orange", "blue", "gray", "yellow"])
                )

                for _ in range(7):
                    object.forward(100)
                    object.right(51.5)
            case 8:
                object.pencolor(
                    choice(["red", "green", "orange", "blue", "gray", "yellow"])
                )

                for _ in range(8):
                    object.forward(100)
                    object.right(45)
            case 9:
                object.pencolor(
                    choice(["red", "green", "orange", "blue", "gray", "yellow"])
                )

                for _ in range(9):
                    object.forward(100)
                    object.right(40)
            case 10:
                object.pencolor(
                    choice(["red", "green", "orange", "blue", "gray", "yellow"])
                )

                for _ in range(10):
                    object.forward(100)
                    object.right(36)


def main():
    timmy = Turtle()
    screen = Screen()

    make_geometric_figures(timmy)

    screen.exitonclick()


if __name__ == '__main__':
    main()
