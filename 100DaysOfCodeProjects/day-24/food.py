import random
from turtle import Turtle


# Create food.
class Food(Turtle):
    # Creates the food.
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('white')
        self.speed('fastest')
        self.refresh()


    # Moves food to a random location on the screen.
    def refresh(self):
        x_random = random.randint(-280, 280)
        y_random = random.randint(-280, 280)
        self.goto(x_random, y_random)


