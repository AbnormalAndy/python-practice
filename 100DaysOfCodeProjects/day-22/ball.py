from turtle import Turtle


COLOR = 'white'
SHAPE = 'circle'
SPEED = 'fastest'


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color(COLOR)
        self.shape(SHAPE)
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed(SPEED)


# TO-DO
# - Get ball to move.
# - Move a set speed.
# - Randomly determine a direction.
# - Reflect angle when bouncing.
