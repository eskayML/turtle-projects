import turtle
import random
import sys
from datetime import datetime

t = turtle.Turtle()

i = 180
c = i * 10

print("\nProcess START: " + str(datetime.now()))

for j in range(i):
    myPenColor1 = float(random.randint(0, c))/c
    myPenColor2 = float(random.randint(0, c))/c
    myPenColor3 = float(random.randint(0, c))/c
    t.pencolor(myPenColor1, myPenColor2, myPenColor3)
    t.forward(j*2)
    t.right(j)

if t.isvisible():
    t.hideturtle()

print("Process END: " + str(datetime.now()))

print("Please close graphics window to end program.")

turtle.mainloop()
