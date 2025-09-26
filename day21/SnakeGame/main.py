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

    while True:
        screen.update()
        sleep(0.1)

        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()

            score.add_counter()

    screen.exitonclick()


if __name__ == "__main__":
    main()
    