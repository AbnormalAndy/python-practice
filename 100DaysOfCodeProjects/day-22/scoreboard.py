from turtle import Turtle


ALIGNMENT = 'center'
FONT = ('futura', 36, 'normal')


PLAYER_ONE = 'player'
PLAYER_TWO = 'computer'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.teleport(0, 250)
        self.ht()
        self.color('white')
        self.score_player = 0
        self.score_computer = 0
        self.player = PLAYER_ONE
        self.computer = PLAYER_TWO
        self.update_score()


    def update_score(self):
        self.write(f"{self.score_computer} : {self.score_player}", align=ALIGNMENT, font=FONT)

    
    def increase_score_player(self):
        self.score_player += 1
        self.clear()
        self.update_score()


    def increase_score_computer(self):
        self.score_computer += 1
        self.clear()
        self.update_score()


    def game_over(self, player):
        self.teleport(0, 0)
        self.write(f"{player.capitalize()} wins!", align=ALIGNMENT, font=FONT)


