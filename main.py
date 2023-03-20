from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

left_paddle = Paddle(-350, 0)
right_paddle = Paddle(350, 0)
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(left_paddle.go_down, "s")
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(right_paddle.go_down, "Down")
screen.onkeypress(right_paddle.go_up, "Up")

game_is_on = scoreboard.r_score < 10 or scoreboard.l_score<10
while game_is_on:
    time.sleep(ball.ball_speed)
    ball.move()
    screen.update()

    # Detect the collision with  upper amd lower walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with the paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 330 or ball.distance(left_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    #Detect if the right player missed the ball:
    if ball.xcor() > 360:
        ball.reset_position()
        scoreboard.l_point()

    #Detect if the right player missed the ball:
    if ball.xcor() < -360:
        ball.reset_position()
        scoreboard.r_point()
    if  scoreboard.r_score == 10 or scoreboard.l_score == 10:
        game_is_on = False
        scoreboard.result()


screen.exitonclick()
