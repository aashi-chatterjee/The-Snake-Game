from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.display_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.score += 1
        self.display_score()

    def display_score(self):
        self.write(arg=f"Score = {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", align=ALIGNMENT, font=FONT)
