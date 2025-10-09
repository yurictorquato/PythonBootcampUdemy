from random import random
from turtle import Screen
from time import sleep

from day23.TrafficGame.car import Car
from day23.TrafficGame.player import Player
from day23.TrafficGame.scoreboard import Scoreboard


def main() -> None:
    screen = Screen()

    screen.setup(width=600, height=600)
    screen.title("Traffic Game")
    screen.tracer(0)

    turtle = Player()
    score = Scoreboard()

    cars = []

    screen.listen()
    screen.onkey(turtle.move_up, "Up")
    screen.onkey(turtle.move_down, "Down")

    is_game_on = True
    while is_game_on:
        sleep(0.1)

        if random() < 0.05:
            for _ in range(5):
                car = Car()
                cars.append(car)

        for car in cars:
            car.move()

            # Detect collision with car
            if turtle.distance(car) < 20:
                is_game_on = False
                score.game_over()

        if turtle.ycor() == 280:
            score.add_level()
            turtle.initial_position()

            # Finish the game with a win
            if score.level == 5:
                is_game_on = False
                score.win_game()

        screen.update()

    screen.exitonclick()


if __name__ == "__main__":
    main()
