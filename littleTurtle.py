from turtle import Turtle


class LittleTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(0, -300)

        self.setheading(90)

    def up(self):
        self.setheading(90)
        self.forward(20)

    def rightt(self):
        self.setheading(0)
        self.forward(20)

    def leftt(self):
        self.setheading(180)
        self.forward(20)
