from turtle import Turtle
import random


class Food(Turtle):    # Food class inheriting from the Turtle class
    def __init__(self):
        super().__init__()  # to inherit Turtle's init
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.color("yellow")
        self.speed("fastest")
        self.reposition()

    def reposition(self):
        random_xcor = random.randint(-280, 280)
        random_ycor = random.randint(-280, 280)
        self.goto(random_xcor, random_ycor)
