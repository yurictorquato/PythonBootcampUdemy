from time import sleep
from turtle import Screen

from day22.PongGame.ball import Ball
from day22.PongGame.line import Line
from day22.PongGame.paddle import Paddle
from day22.PongGame.score import Scoreboard


LEFT = -200
RIGHT = 180


def main():
    screen = Screen()

    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Pong Game")

    line = Line()
    ball = Ball()
    right_paddle = Paddle(350)
    left_paddle = Paddle(-350)
    right_score = Scoreboard(RIGHT)
    left_score = Scoreboard(LEFT)

    screen.listen()
    screen.onkey(key="Up", fun=right_paddle.go_up)
    screen.onkey(key="Down", fun=right_paddle.go_down)
    screen.onkey(key="w", fun=left_paddle.go_up)
    screen.onkey(key="s", fun=left_paddle.go_down)

    is_game_on = True
    while is_game_on:
        screen.update()
        sleep(ball.move_speed)

        ball.move()

        # Detect collision with wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        # Detect collision with paddle
        if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
            ball.bounce_x()

        # Detect if the ball has passed the right paddle
        if ball.xcor() >= 400:
            left_score.add_counter()
            ball.reset_position()

        # Detect if the ball has passed the left paddle
        if ball.xcor() <= -400:
            right_score.add_counter()
            ball.reset_position()

        # Finish the game
        if right_score.counter == 5 or left_score.counter == 5:
            is_game_on = False

    screen.exitonclick()


if __name__ == '__main__':
    main()
