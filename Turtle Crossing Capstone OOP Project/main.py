import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(height=600, width=600)
screen.tracer(0)


player = Player()
car_manager = CarManager()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(key="Up", fun=player.move_up)


game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.cars_move()

    # Detect collion with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect successful turtle crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()






screen.exitonclick()