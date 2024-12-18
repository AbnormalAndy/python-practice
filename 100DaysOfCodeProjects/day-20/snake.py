from turtle import Turtle


STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        

    # Create snake.
    def create_snake(self):
        for position in STARTING_POSITION:
            segment = Turtle('square')
            segment.color('white')
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)

        
    # Move forward.
    def move(self):
        for segment_number in range(len(self.segments) - 1, 0, -1):
            x_new = self.segments[segment_number - 1].xcor()
            y_new = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(x_new, y_new)

        
        self.segments[0].forward(MOVE_DISTANCE)


    # Sets direction up if the direction is not down.
    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)


    # Sets direction down if the direction is not up.
    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)


    # Sets direction left if the direction is not right.
    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)


    # Sets direction right if the direction is not left.
    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)
