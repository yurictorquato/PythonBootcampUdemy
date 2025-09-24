from time import sleep
from turtle import Screen, Turtle


def make_snake(screen) -> list[Turtle]:
    x = 0

    segments = []

    for _ in range(3):
        snake = Turtle("square")

        snake.color("white")
        snake.penup()
        snake.goto(x, 0)

        screen.update()

        segments.append(snake)

        x -= 20

    return segments


def left(object: Turtle):
    object.left(90)


def right(object: Turtle):
    object.right(90)


def snake_game(object: list[Turtle], screen) -> None:
    while True:
        screen.update()

        for segment in object:
            segment.forward(10)
            segment.speed("fast")

            sleep(0.1)

            screen.listen()
            screen.onkey(key="a", fun=lambda: left(segment))
            screen.onkey(key="d", fun=lambda: right(segment))


def main():
    screen = Screen()

    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)

    snake = make_snake(screen)
    snake_game(snake, screen)

    screen.exitonclick()
    

if __name__ == '__main__':
    main()
