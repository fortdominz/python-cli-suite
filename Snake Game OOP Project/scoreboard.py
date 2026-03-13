
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Times New Roman", 15, "normal")

with open("data.txt") as data:
    num = int(data.read())

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = num
        self.color("white")
        self.penup()
        self.goto(0, 275)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}    High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.score = 0
        with open("data.txt", mode="w") as data:
            data.write(f"{self.high_score}")
        self.update_scoreboard()



    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)
