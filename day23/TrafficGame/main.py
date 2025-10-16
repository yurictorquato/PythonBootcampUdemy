from turtle import Screen
from time import sleep

from day23.TrafficGame.car import CarManager
from day23.TrafficGame.player import Player
from day23.TrafficGame.scoreboard import Scoreboard


def main() -> None:
    screen = Screen()

    screen.setup(width=600, height=600)
    screen.title("Traffic Game")
    screen.tracer(0)

    turtle = Player()
    score = Scoreboard()
    car_manager = CarManager()

    screen.listen()
    screen.onkey(turtle.move_up, "Up")
    screen.onkey(turtle.move_down, "Down")

    is_game_on = True
    while is_game_on:
        sleep(0.1)

        car_manager.add_car()
        car_manager.move_all_cars()

        # Detect collision with car
        for car in car_manager.cars:
            if turtle.distance(car) < 20:
                is_game_on = False
                score.game_over()

        # Detect successful crossing line
        if turtle.is_at_finish_line():
            score.add_level()
            turtle.initial_position()
            car_manager.move_faster()

            # Finish the game with a win
            if score.level == 5:
                is_game_on = False
                score.win_game()

        screen.update()

    screen.exitonclick()


if __name__ == "__main__":
    main()
