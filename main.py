from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Screen start
screen = Screen()
screen.setup(width=900, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("PONG")

# Paddle setup
paddle = Paddle()
paddle.can_move()

# Ball setup
ball = Ball()

# Scoreboard setup
scoreboard = Scoreboard()

game_is_on = True
# serve = screen.textinput()
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move_forward()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    if ball.distance(paddle.right_paddle) < 50 and ball.xcor() > 380:
        ball.hit_paddle()
    elif ball.distance(paddle.left_paddle) < 50 and ball.xcor() < -380:
        ball.hit_paddle()
    elif ball.xcor() > 450:
        ball.home()
        scoreboard.add_point("left")
    elif ball.xcor() < -450:
        ball.home()
        scoreboard.add_point("right")
    elif scoreboard.score_left == 5 or scoreboard.score_right == 5:
        game_is_on = False
        ball.hideturtle()
        ball.write(f"{scoreboard.winner()} won!", align="center", font=("Courier", 50, "normal"))
    screen.update()

screen.exitonclick()

