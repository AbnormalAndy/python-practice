from turtle import Turtle


COLOR = 'white'
SHAPE = 'circle'
MOVEMENT = 5


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color(COLOR)
        self.shape(SHAPE)
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)


    def move(self):
        self.forward(MOVEMENT)


    def refresh(self):
        self.goto(0, 0)


