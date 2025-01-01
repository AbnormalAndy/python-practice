from turtle import Turtle


COLOR = 'white'
SHAPE = 'square'


MOVE_DISTANCE = 20


UP = 90
DOWN = 270


class Paddle:
    def __init__(self, starting_position):
        self.starting_position = starting_position
        self.segments = []
        self.create_paddle_player()
        self.paddle_top = self.segments[0]
        self.paddle_bottom = self.segments[-1]
        self.paddle_top.setheading(UP)
        self.paddle_bottom.setheading(DOWN)


    # Create the paddle with the number of tuples in starting_position list.
    def create_paddle_player(self):
        for position in self.starting_position:
            self.add_segment(position)


    # Add segments to the paddle.
    def add_segment(self, position):
        segment = Turtle()
        segment.penup()
        segment.color(COLOR)
        segment.shape(SHAPE)
        segment.goto(position)
        self.segments.append(segment)


    # Move segments up, leading by first item in the list.
    def move_up(self):
        if self.paddle_top.ycor() < 300:
            for segment_number in range(len(self.segments) - 1, 0, -1):
                x_new = self.segments[segment_number - 1].xcor()
                y_new = self.segments[segment_number - 1].ycor()
                self.segments[segment_number].goto(x_new, y_new)


            self.paddle_top.forward(MOVE_DISTANCE)


    # Move segments down, leading by last item in the list.
    def move_down(self):
        if self.paddle_bottom.ycor() > -300:
            for segment_number in range(len(self.segments) - 1):
                x_new = self.segments[segment_number + 1].xcor()
                y_new = self.segments[segment_number + 1].ycor()
                self.segments[segment_number].goto(x_new, y_new)


            self.paddle_bottom.forward(MOVE_DISTANCE)


