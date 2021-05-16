from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.number = 0
        self.color("black")
        self.penup()
        self.goto(-260, 280)
        self.hideturtle()
        self.score_writing()

    def score_writing(self):
        self.write(f"Score: {self.number}", align="center", font=("Arial", 14, "normal"))

    def score_update(self):
        self.number += 1
        self.clear()
        self.score_writing()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 14, "normal"))
