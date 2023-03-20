from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 220)
        self.write(self.l_score, align="center", font=("Courier", 60, "normal"))
        self.goto(100, 220)
        self.write(self.r_score, align="center", font=("Courier", 60, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update()

    def r_point(self):
        self.r_score += 1
        self.update()

    def result(self):
        self.goto(0, 0)
        if self.l_score == 1:
            self.write("Left player won!!", align="center", font=("Courier", 40, "normal"))
        if self.r_score == 10:
            self.write("Right player won!!", align="center", font=("Courier", 40, "normal"))

