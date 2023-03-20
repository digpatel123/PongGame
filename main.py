from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

left_paddle = Paddle(-350, 0)
right_paddle = Paddle(350, 0)
ball = Ball()
screen.update()

game_is_on = True

screen.listen()
screen.onkey(left_paddle.go_down, "s")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(right_paddle.go_up, "Up")

while game_is_on:
    time.sleep(0.1)
    ball.move()
    screen.update()

    # Detect the collision with  upper amd lower walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with the paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 330 or ball.distance(left_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

screen.exitonclick()
