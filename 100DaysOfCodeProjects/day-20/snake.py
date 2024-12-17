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


