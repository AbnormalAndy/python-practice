from turtle import Turtle


COLOR = 'white'


YCOR_SOLID = [-260, -220, -180, -140, -100, -60, -20, 20, 60, 100, 140, 180, 220, 260]
YCOR_STRIPE = [-240, -200, -160, -120, -80, -40, 40, 80, 120, 160, 200, 240]


class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.color(COLOR)
        self.line_solid()
        self.line_stripe()


    # Create solid lines.
    def line_solid(self):
        for i in YCOR_SOLID:
            self.teleport(350, i)
            self.goto(-350, i)
            

    # Create striped lines.
    def line_stripe(self):
        for i in YCOR_STRIPE:
            self.teleport(350, i)
            while self.xcor() > -350:
                self.backward(70)
                self.penup()
                self.backward(70)
                self.pendown()


