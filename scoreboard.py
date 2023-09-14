from turtle import Turtle

ALIGN = "center"
FONT = ('Arial', 12, 'normal')
GAMEOVER_FONT = ("courier", 24, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-30, 250)
        self.write(f"Score : {self.score}", align=ALIGN, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over", align=ALIGN, font=GAMEOVER_FONT)
