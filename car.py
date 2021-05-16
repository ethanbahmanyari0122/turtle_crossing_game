from turtle import Turtle
import random

COLORS = ["red", "blue", "green", "yellow", "purple", "orange"]
SPEED = [0, 1, 2, 3, 4, 5]


class Car():
    def __init__(self):
        self.cars = []

    def move(self):
        for car in self.cars:
            car.forward(20)

    def creatCar(self):
        number = random.randint(0, 6)
        if number == 1 or number == 2:
            car = Turtle("square")
            car.penup()
            car.setheading(180)
            car.color(COLORS[random.randint(0, 5)])
            car.goto(300, random.randint(-250, 250))
            self.cars.append(car)
