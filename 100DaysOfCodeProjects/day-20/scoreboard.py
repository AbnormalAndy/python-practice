from turtle import Turtle


# Constants
ALIGNMENT = 'center' 
FONT = ('Courier', 12, 'normal')


class Scoreboard(Turtle):
    # Creates scoreboard.
    def __init__(self):
        super().__init__()
        self.teleport(0, 270)
        self.ht()
        self.color('white')
        self.score = 0
        self.update_score()


    # Updates score.
    def update_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    
    def game_over(self):
        self.teleport(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)


    # Increases score.
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

   
