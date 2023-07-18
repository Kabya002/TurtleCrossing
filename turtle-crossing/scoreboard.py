from turtle import Turtle
FONT_1 = ("Courier", 15, "normal")
FONT_2 = ("Courier", 24, "normal")
ALIGNMENT = "left"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(-270, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.score}", align=ALIGNMENT, font=FONT_1)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT_2)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
