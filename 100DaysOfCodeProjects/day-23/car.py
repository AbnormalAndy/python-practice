from turtle import Turtle


SHAPE = 'square'


class Car(Turtle):
    def __init__(self, random_color, xcor_position, ycor_position, random_speed):
        super().__init__()
        self.penup()
        self.shape(SHAPE)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random_color)
        self.speed = random_speed
        self.goto(xcor_position, ycor_position)


    # Move car to the left of the screen.
    def move_car_left(self):
        x_new = self.xcor() - self.speed
        self.goto(x_new, self.ycor())


    # Move car to the right of the screen.
    def move_car_right(self):
        x_new = self.xcor() + self.speed
        self.goto(x_new, self.ycor())


    # Move car to its starting point.
    def reset(self, xcor_start):
        self.goto(xcor_start, self.ycor())


    # Increase car speed.
    def increase_speed(self):
        self.speed *= 1.2


