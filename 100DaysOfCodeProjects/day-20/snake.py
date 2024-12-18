from turtle import Turtle


STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]
        

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

        
        self.snake_head.forward(MOVE_DISTANCE)


    # Sets direction up if the direction is not down.
    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)


    # Sets direction down if the direction is not up.
    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)


    # Sets direction left if the direction is not right.
    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)


    # Sets direction right if the direction is not left.
    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)


