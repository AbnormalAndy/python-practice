from turtle import Turtle


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.teleport(0, 270)
        self.ht()
        self.color('white')
        self.score = 0
        self.write(f"Score: {self.score}", align='center', font=('Arial', 12, 'normal'))


    def refresh(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align='center', font=('Arial', 12, 'normal'))

        
