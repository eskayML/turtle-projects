from turtle import Screen,Turtle 
import time

ALIGNMENT="center"
FONT=("Courier", 80, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score,align=ALIGNMENT,font=FONT)
        self.goto(100,200)
        self.write(self.r_score,align=ALIGNMENT,font=FONT)
        
    def l_point(self):
        self.l_score += 1
        self.update_score()
    
    def r_point(self):
        self.r_score += 1
        self.update_score()
    
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",align=ALIGNMENT,font=FONT)
        
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(position)
    
    def go_up(self):
        new_y = self.ycor()+20
        self.goto(self.xcor(),new_y)
        
    def go_down(self):
        new_y = self.ycor()-20
        self.goto(self.xcor(),new_y)
        
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.09
    
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)
    
    def bounce_y(self):
        self.y_move*=-1

    def bounce_x(self):
        self.x_move*=-1
        self.move_speed *= 0.8
    
    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.09
        self.bounce_x()

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
