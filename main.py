from turtle import Screen
from littleTurtle import LittleTurtle
from car import Car
from scoreboard import Scoreboard
import time
screen = Screen()
screen.screensize(600, 600)
screen.title("Turtle Crossing")
screen.tracer(0)
turtlee = LittleTurtle()
cars = Car()
score = Scoreboard()
screen.listen()
screen.onkey(turtlee.up, "w")
screen.onkey(turtlee.rightt, "d")
screen.onkey(turtlee.leftt, "a")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    cars.creatCar()
    cars.move()
    for car in cars.cars:
        if turtlee.distance(car) < 20:
            game_is_on = False
            score.game_over()
    if turtlee.ycor() > 300:
        score.score_update()
        turtlee.goto(0, -300)



screen.exitonclick()
