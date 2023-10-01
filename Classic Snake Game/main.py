import time
from turtle import Screen
from snake import Snake
from food import Food
from score import Score


def Screen_setup():
    screen.setup(width=600, height=600)
    screen.bgcolor("black")

def game():
    Screen_setup()
    screen.title("Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    score = Score()

    screen.listen()
    screen.onkey(snake.up,'Up')
    screen.onkey(snake.down,'Down')
    screen.onkey(snake.left,'Left')
    screen.onkey(snake.right,'Right')

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        #Detect the collision with food
        if snake.head.distance(food) < 15:
            food.refresh_food_location()
            score.increase_score()
            snake.extend()
            
        #Detect the collision with wall
        if snake.head.xcor() >280 or snake.head.xcor() <-280 or snake.head.ycor() > 280 or snake.head.ycor() <-280:
            game_is_on = False
            score.game_over()
            
        #Detect the collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment)<10:
                game_is_on = False
                score.game_over()

screen = Screen()
Screen_setup()

while screen.textinput("Snake Game", "Do you want to play Snake Game? y/n:").lower() == "y":
    game()
    time.sleep(2)
    screen.clearscreen()
    Screen_setup()
