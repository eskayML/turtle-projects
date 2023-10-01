from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

def Screen_setup():
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.title("Pong")
    screen.tracer(0)

def game():
    Screen_setup()
    r_paddle = Paddle((350, 0))
    l_paddle = Paddle((-350, 0))
    ball = Ball()
    score = Score()

    screen.listen()
    screen.onkey(r_paddle.go_up, "Up")
    screen.onkey(r_paddle.go_down, "Down")
    screen.onkey(l_paddle.go_up, "w")
    screen.onkey(l_paddle.go_down, "s")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(ball.move_speed)
        ball.move()

        #Detect collision with wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        #Detect collision with paddle
        if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
            ball.bounce_x()

        #Detect R paddle misses
        if ball.xcor() > 380:
            ball.reset_position()
            score.l_point()

        #Detect L paddle misses:
        if ball.xcor() < -380:
            ball.reset_position()
            score.r_point()
        
        if score.l_score == 5:
            score.game_over()
            game_is_on = False
            
        if score.r_score == 5:
            score.game_over()
            game_is_on = False
        
screen = Screen()
Screen_setup()
while screen.textinput("Ping-Pong Game", "Do you want to play Pong Game? y/n:").lower() == "y":
    game()
    time.sleep(3)
    screen.clearscreen()
    Screen_setup()
