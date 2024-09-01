# The apple halves move randomly for 5 seconds.
# After 5 seconds, they come together, and a stem and leaf appear on top, making the apple look more complete.
# The window remains open until manually closed, displaying the complete apple.

import turtle
import time
import random


screen = turtle.Screen()
screen.title("Apple Parts Coming Together")
screen.bgcolor("black")
screen.setup(width=800, height=600)

apple_part1 = turtle.Turtle()
apple_part2 = turtle.Turtle()

apple_part1.shape("circle")
apple_part2.shape("circle")

apple_part1.color("green")
apple_part2.color("green")

apple_part1.shapesize(stretch_wid=5, stretch_len=5)
apple_part2.shapesize(stretch_wid=5, stretch_len=5)

apple_part2.goto(50, 0)
apple_part1.penup()
apple_part2.penup()

stem_leaf = turtle.Turtle()
stem_leaf.hideturtle()
stem_leaf.penup()

def move_parts():
    screen_width, screen_height = screen.window_width(), screen.window_height()
    new_x1 = random.randint(-screen_width//2 + 50, screen_width//2 - 50)
    new_y1 = random.randint(-screen_height//2 + 50, screen_height//2 - 50)
    new_x2 = random.randint(-screen_width//2 + 50, screen_width//2 - 50)
    new_y2 = random.randint(-screen_height//2 + 50, screen_height//2 - 50)

    apple_part1.goto(new_x1, new_y1)
    apple_part2.goto(new_x2, new_y2)


def bring_together():
    apple_part1.goto(-25, 0)
    apple_part2.goto(25, 0)


    stem_leaf.goto(0, 50)
    stem_leaf.color("brown")
    stem_leaf.pendown()
    stem_leaf.pensize(5)
    stem_leaf.setheading(90)
    stem_leaf.forward(30)


    stem_leaf.color("green")
    stem_leaf.begin_fill()
    stem_leaf.circle(15, 180)
    stem_leaf.left(90)
    stem_leaf.circle(15, 180)
    stem_leaf.end_fill()


start_time = time.time()
while time.time() - start_time < 5:
    move_parts()
    time.sleep(0.1)

bring_together()

screen.mainloop()
