from turtle import Turtle


COLOR = 'white'


ALIGN_SCOREBOARD = 'left'
ALIGN_GAME_OVER = 'center'


FONT = ('futura', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.teleport(-290, 260)
        self.color(COLOR)
        self.ht()
        self.penup()
        self.score = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(f"Level: {self.score}", align=ALIGN_SCOREBOARD, font=FONT) 


    def increase_level(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


    def game_over(self):
        self.teleport(0, -20)
        self.write(f"GAME OVER", align=ALIGN_GAME_OVER, font=FONT)


