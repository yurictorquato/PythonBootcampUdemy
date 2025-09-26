from turtle import Turtle


MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self) -> None:
        self.segments = self.make_snake()
        self.head = self.segments[0]

    
    def make_snake(self) -> list:
        x = 0

        segments = []

        for _ in range(3):
            snake = Turtle(shape="square")

            snake.color("white")
            snake.penup()
            snake.goto(x, 0)

            segments.append(snake)

            x -= 20

        return segments
    

    def up(self) -> None:
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def down(self) -> None:
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self) -> None:
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self) -> None:
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def move(self) -> None:
        for segment in range((len(self.segments) - 1), 0, -1):
            x = self.segments[segment - 1].xcor()
            y = self.segments[segment - 1].ycor()
            
            self.segments[segment].goto(x, y)

        self.head.forward(MOVE_DISTANCE)
