from turtle import Turtle


COLOR = 'white'
SHAPE = 'square'
MOVE_DISTANCE = 20
STARTING_POSITION_PLAYER = [(550, 20), (550, 0), (550, -20)]
#STARTING_POSITION_COMPUTER = [(-550, 20), (-550, 0), (-550, -20)]


UP = 90
DOWN = 270


class Paddle:
    def __init__(self):
        self.segments = []
        self.create_paddle_player()
        self.paddle_top = self.segments[0]
        self.paddle_bottom = self.segments[2]
        self.paddle_top.setheading(UP)
        self.paddle_bottom.setheading(DOWN)


    def create_paddle_player(self):
        for position in STARTING_POSITION_PLAYER:
            self.add_segment(position)


    def add_segment(self, position):
        segment = Turtle()
        segment.penup()
        segment.color(COLOR)
        segment.shape(SHAPE)
        segment.goto(position)
        self.segments.append(segment)


    def move_up(self):
        for segment_number in range(len(self.segments) - 1, 0, -1):
            x_new = self.segments[segment_number - 1].xcor()
            y_new = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(x_new, y_new)


        self.paddle_top.forward(MOVE_DISTANCE)


    def move_down(self):
        for segment_number in range(len(self.segments) - 1):
            x_new = self.segments[segment_number + 1].xcor()
            y_new = self.segments[segment_number + 1].ycor()
            self.segments[segment_number].goto(x_new, y_new)


        self.paddle_bottom.forward(MOVE_DISTANCE)


# TO-DO
# Move up and down.
# - Need to iterate through the segments.
#     - Move each segment by MOVE_DISTANCE.
#     - Move up by leading with first position?
#     - Move down by leading with last position?

# - Set border limits.
#     - Main or Paddle file?


