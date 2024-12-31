from turtle import Turtle


COLOR = 'white'
SHAPE = 'square'
MOVE_DISTANCE = 20
STARTING_POSITION = [(550, 20), (550, 0), (550, -20)]


class Paddle:
    def __init__(self):
        self.segments = []
        self.create_paddle()


    def create_paddle(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

        
    def add_segment(self, position):
        segment = Turtle()
        segment.penup()
        segment.color(COLOR)
        segment.shape(SHAPE)
        segment.goto(position)
        self.segments.append(segment)


