from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid = 0.5)
        self.color("red")
        self.speed("fastest")
        random_x = randint(-280,280)
        random_y = randint(-280,270)
        self.goto(random_x, random_y)
        self.refresh_food_location()

    def refresh_food_location(self):
        random_x = randint(-280,280)
        random_y = randint(-280,280)
        self.goto(random_x, random_y)