from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial",20,"normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(0,270)
        self.score = 0
        self.current_score()
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.current_score()

    def current_score(self):
        self.write(f"Score: {self.score}",align=ALIGNMENT,font=FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",align=ALIGNMENT,font=FONT)