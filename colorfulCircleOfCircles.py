import turtle
import random
import sys
from datetime import datetime

t = turtle.Turtle()

i = 36

#t.setx(-250)
#t.sety(-250)

print("\nProcess START: " + str(datetime.now()))

for x in range(8):
    for j in range(i):
        myPenColorR = random.random()
        myPenColorG = random.random()
        myPenColorB = random.random()

        t.pencolor(myPenColorR, myPenColorG, myPenColorB)
        t.forward(250)
        t.right(170)
    t.left(45)

if t.isvisible():
    t.hideturtle()

print("Process END: " + str(datetime.now()))

print("Please close graphics window to end program.")

turtle.mainloop()
