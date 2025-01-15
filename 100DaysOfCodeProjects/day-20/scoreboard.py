from turtle import Turtle
import os


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
        self.high_score = 0
        self.score = 0
        self.update_score()


    # Updates score.
    def update_score(self):
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    
    def game_over(self):
        self.teleport(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)


    # Increases score.
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()


    # Reads high_score.txt file if it exists to set the high score.
    def high_score_read(self):
        if os.path.exists('high_score.txt'):
            with open('high_score.txt', mode='r') as file:
                      self.high_score = int(file.read())
            self.clear()
            self.update_score()
        else:
            self.high_score = 0

   
    # Writes a new high score if there is one.
    def high_score_write(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open('high_score.txt', mode='w') as file:
            file.write(str(self.high_score))


