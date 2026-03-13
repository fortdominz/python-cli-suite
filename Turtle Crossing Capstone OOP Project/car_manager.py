from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVING_SPEED = 10

STARTING_POSITION_X = 280


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        chance = random.randint(1,6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            y = random.randint(a=-260, b=260)
            new_car.goto(STARTING_POSITION_X, y)
            new_car.setheading(180)
            self.all_cars.append(new_car)


    def cars_move(self):
        for car in self.all_cars:
            x = car.xcor()
            x -= self.car_speed
            car.goto(x, car.ycor())


    def level_up(self):
        self.car_speed += MOVING_SPEED
