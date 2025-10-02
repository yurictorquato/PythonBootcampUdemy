from turtle import Screen

from platform import Platform
from line import Line


def main():
    screen = Screen()

    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Ping Pong Game")

    line = Line()
    paddle = Platform()

    screen.listen()
    screen.onkey(key="Up", fun=paddle.up)
    screen.onkey(key="Down", fun=paddle.down)

    screen.exitonclick()


if __name__ == '__main__':
    main()
