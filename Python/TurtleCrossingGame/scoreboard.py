from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-270, -270)
        self.write(self.score, align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def final_score(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER\nFinal Score: {self.score}", align="center", font=FONT)