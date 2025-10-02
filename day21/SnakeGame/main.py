from turtle import Screen
from score import Score
from food import Food
from snake import Snake
from time import sleep


def main():
    screen = Screen()

    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    score = Score()

    screen.listen()
    screen.onkey(key="Up", fun=snake.up)
    screen.onkey(key="Down", fun=snake.down)
    screen.onkey(key="Left", fun=snake.left)
    screen.onkey(key="Right", fun=snake.right)

    game_is_on = True
    while game_is_on:
        screen.update()
        sleep(0.1)

        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            score.add_counter()

        # Detect collision with wall
        if (snake.head.xcor() > 290 or snake.head.xcor() < -290) or (snake.head.ycor() > 290 or snake.head.ycor() < -290):
            score.game_over()
            game_is_on = False

        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                score.game_over()
                game_is_on = False

    screen.exitonclick()


if __name__ == "__main__":
    main()
    