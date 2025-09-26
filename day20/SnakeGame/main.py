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


def left(object: list[Turtle]):   
    object[0].left(90)


def right(object: list[Turtle]):
    object[0].right(90)


def snake_game(object: list[Turtle], screen) -> None:
    while True:
        screen.update()
        sleep(0.1)

        for segment in range((len(object) - 1), 0, -1):
            x = object[segment - 1].xcor()
            y = object[segment - 1].ycor()
            
            object[segment].goto(x, y)

        object[0].forward(10)

        # screen.listen()
        # screen.onkey(key="a", fun=lambda: left(object))
        # screen.onkey(key="d", fun=lambda: right(object))



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
