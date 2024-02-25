import turtle
import random
import sys
from datetime import datetime

t = turtle.Turtle()

i = 50
t.left(90)

limitX, limitY = t.screen.screensize()

print("\nProcess START: " + str(datetime.now()))

for j in range(i):
    myPenColorR = random.random()
    myPenColorG = random.random()
    myPenColorB = random.random()

    t.pencolor(myPenColorR, myPenColorG, myPenColorB)
    t.forward(i)
    turn = random.randint(1, 359)
    t.right(turn)

    tx, ty = t.position()
    if tx < (-1 * limitX) or tx > limitX or ty < (-1 * limitY) or ty > limitY:
        t.goto(0, 0)


if t.isvisible():
    t.hideturtle()

print("Process END: " + str(datetime.now()))

print("Please close graphics window to end program.")

turtle.mainloop()
