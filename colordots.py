import turtle
import random
import sys
from datetime import datetime

if len(sys.argv) < 3:
    print("Please call this program as follows:")
    print("    colordots.py lolim hilim")
    print("where lolim and hilim are integers and lolim <= hilim")
    exit()

try:
    dotsLower = int(sys.argv[1])
except ValueError:
    print("The value for the LOWER limit of the number of dots must be an integer")
    exit()

try:
    dotsUpper = int(sys.argv[2])
except ValueError:
    print("The value for the UPPER limit of the number of dots must be an integer")
    exit()

if dotsUpper >= dotsLower:
    numDots = random.randint(dotsLower, dotsUpper)
    print(str(numDots) + " dots will be plotted")
else:
    print("The value for the upper limit of dots must be larger than the value for the lower limit.")
    exit()

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor(0, 0, 0)
t.pencolor("white")
t.hideturtle()

c = turtle.Turtle()
c.pencolor("white")
c.hideturtle()

limitX, limitY = t.screen.screensize()

t.penup()
c.penup()
c.goto(limitX, limitY)

print("\nProcess START: " + str(datetime.now()))

for i in range(numDots):
    tx, ty = t.position()
    t.forward(1)
    t.penup()
    angle = random.randint(1, 359)
    t.right(angle)
    skip = random.randint(1, 100)
    t.forward(skip)
    if tx < (-1 * limitX) or tx > limitX or ty < (-1 * limitY) or ty > limitY:
        x = random.randint(-1 * limitX, limitX)
        y = random.randint(-1 * limitY, limitY)
        t.goto(x, y)

    c.clear()
    c.write(str(i+1) + " of " + str(numDots))
    j = random.randint(0, 99)
    t.pencolor(random.random(), random.random(), random.random())

    t.pendown()

if t.isvisible():
    t.hideturtle()

print("Process END: " + str(datetime.now()))
print("Please close graphics window to end program.")

turtle.mainloop()
