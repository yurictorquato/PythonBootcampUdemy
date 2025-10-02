from turtle import Screen

from platform import Platform
from line import Line


def main():
    screen = Screen()

    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Ping Pong Game")

    line = Line()
    right_paddle = Platform(350)
    left_paddle = Platform(-350)

    screen.listen()
    screen.onkey(key="Up", fun=right_paddle.up)
    screen.onkey(key="Down", fun=right_paddle.down)
    screen.onkey(key="Up", fun=left_paddle.up)
    screen.onkey(key="Down", fun=left_paddle.down)

    screen.exitonclick()


if __name__ == '__main__':
    main()
