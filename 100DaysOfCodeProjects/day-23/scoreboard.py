from turtle import Turtle


COLOR = 'white'


ALIGN = 'left'
FONT = ('futura', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.teleport(-280, 250)
        self.color(COLOR)
        self.ht()
        self.penup()
        self.score = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(f"Level: {self.score}", align=ALIGN, font=FONT) 


    def increase_level(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


