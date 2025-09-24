from random import randint
from turtle import Screen, Turtle, colormode

from colorgram import extract


def get_palette_colors(archive: str, number_of_colors: int) -> list[tuple[int, int, int]]:
    colors = extract(archive, number_of_colors)

    list_colors = []

    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b

        list_colors.append((r, g, b))

    return list_colors


def make_draw(object: Turtle, length: int, list_colors: list[tuple[int, int, int]]) -> None:
    for row in range(length):
        for column in range(length):
            object.penup()
            x = (column * 50) - 200
            y = (row * 50) - 200

            object.goto(x, y)
            object.penup()
            object.dot(20, list_colors[randint(0, (len(list_colors) - 1))])


def main():
    timmy = Turtle()
    screen = Screen()

    timmy.speed("fastest")
    timmy.hideturtle()

    colormode(255)

    list_colors = get_palette_colors("liverpool.jpg", 20)

    make_draw(timmy, 10, list_colors)

    screen.exitonclick()


if __name__ == '__main__':
    main()
