from turtle import Turtle


COLOR = 'white'
SHAPE = 'circle'
MOVEMENT = 4


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color(COLOR)
        self.shape(SHAPE)
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.x_move = 4
        self.y_move = 4


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)


    def refresh(self):
        self.goto(0, 0)


    def bounce_x(self):
        self.x_move *= -1


    def bounce_y(self):
        self.y_move *= -1


