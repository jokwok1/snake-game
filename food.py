from turtle import Turtle
import random

class Food(Turtle):  # inherit from turtle class

    def __init__(self):
        super().__init__()  # call super class
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # half size of circle
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)  # generate random x coordinate from 280 to - 280 based on our screen size
        random_y = random.randint(-280, 280)
        self.goto(random_x,random_y)


