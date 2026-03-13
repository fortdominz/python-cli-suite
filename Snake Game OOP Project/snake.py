from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.squares = []
        self.create_snake()
        self.head = self.squares[0]

    def create_snake(self):
        # Creates Snake
        for position in STARTING_POSITIONS:
            self.add_square(position)

    def add_square(self, position):
        # Adds new squares to the snake body
        neon = Turtle(shape="square", visible=False)
        neon.penup()
        neon.goto(position)
        neon.color("white")
        neon.showturtle()
        self.squares.append(neon)

    def reset_snake(self):
        for square in self.squares:
            square.goto(10000, 10000)
        self.squares.clear()
        self.create_snake()
        self.head = self.squares[0]

    def grow(self):
        # Adds a new square to the snake as it eats
        self.add_square(self.squares[-1].position()) # parameter for the position to add as the last square in the list of squares

    def move(self):
        # Moves Snake
        for num_of_square in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[num_of_square - 1].xcor()
            new_y = self.squares[num_of_square - 1].ycor()
            self.squares[num_of_square].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


