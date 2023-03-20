from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_cord, y_cord):
        super().__init__()
        self.shape_paddle()
        self.goto(x=x_cord, y=y_cord)

    def shape_paddle(self):
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color("white")

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
