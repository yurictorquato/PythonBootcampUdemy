from turtle import Screen, Turtle

from day22.PongGame.line import Line
from day22.PongGame.ball import Ball
from day22.PongGame.paddle import Paddle


def line(object: Turtle):
    object.hideturtle()
    object.penup()
    object.pensize(8)
    object.pencolor("white")
    object.sety(-400)
    object.setheading(90)

    for _ in range(20):
        object.pendown()
        object.forward(30)
        object.penup()
        object.forward(30)


def main():
    screen = Screen()

    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Ping Pong Game")

    # line = Line()
    ball = Ball()
    right_paddle = Paddle(350)
    left_paddle = Paddle(-350)

    # line()

    screen.listen()
    screen.onkey(key="Up", fun=right_paddle.go_up)
    screen.onkey(key="Down", fun=right_paddle.go_down)
    screen.onkey(key="Up", fun=left_paddle.go_up)
    screen.onkey(key="Down", fun=left_paddle.go_down)

    while True:
        ball.move()

        # Detect collision with wall
        if ball.ycor() > 300 or ball.ycor() < -300:
            pass

    screen.exitonclick()


if __name__ == '__main__':
    main()
