from turtle import Turtle, Screen
from paddle import paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

left_paddle = paddle(-350, 0)
right_paddle = paddle(350, 0)
screen.update()


game_is_on = True


screen.listen()
screen.onkey(left_paddle.go_down, "s")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(right_paddle.go_up, "Up")

while game_is_on:
    screen.update()


screen.exitonclick()
