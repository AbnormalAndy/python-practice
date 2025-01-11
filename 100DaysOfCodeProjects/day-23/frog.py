from turtle import Turtle


SHAPE = 'turtle'
COLOR = 'white'


START = (0, -270)
MOVE = 20 


class Frog(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.color(COLOR)
        self.setheading(90)
        self.penup()
        self.goto(START)


    def move_up(self):
        y_new = self.ycor() + MOVE
        self.goto(self.xcor(), y_new)


    def move_right(self):
        if self.xcor() < 270:
            x_new = self.xcor() + MOVE
            self.goto(x_new, self.ycor())


    def move_left(self):
        if self.xcor() > -270:
            x_new = self.xcor() - MOVE
            self.goto(x_new, self.ycor())


    def reset(self):
        self.goto(START)


