import random
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game 1.0")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect snake collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.grow()
        scoreboard.increase_score()

    # Detect Collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset_score()
        snake.reset_snake()

        # Detect collision with tail
    for square in snake.squares[1:]: # slicing here to remove the head of the snake (1st square... [0:1]) from the condition
        if snake.head.distance(square) < 10:
            scoreboard.reset_score()
            snake.reset_snake()





screen.exitonclick()