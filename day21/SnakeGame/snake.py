from turtle import Turtle


STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self) -> None:
        self.segments = []
        self.make_snake()
        self.head = self.segments[0]

    
    def make_snake(self) -> None:
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self, position) -> None:
        snake = Turtle(shape="square")

        snake.color("white")
        snake.penup()
        snake.goto(position)

        self.segments.append(snake)


    def extend(self) -> None:
        self.add_segment(self.segments[-1].position())
    

    def move(self) -> None:
        for segment in range((len(self.segments) - 1), 0, -1):
            x = self.segments[segment - 1].xcor()
            y = self.segments[segment - 1].ycor()

            self.segments[segment].goto(x, y)

        self.head.forward(MOVE_DISTANCE)


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
