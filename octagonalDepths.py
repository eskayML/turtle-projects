import turtle
import sys
from datetime import datetime

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor(0, 0, 0)
#s.bgcolor(1, 1, 1)

t.pencolor("white")
i = 200

print("\nProcess START: " + str(datetime.now()))

for x in range(i):
    f = float(i)
#    print(str(f), str(x), str(x/f))
    t.pencolor(x/f, x/f, x/f)
    t.forward(x)
    t.right(45)

if t.isvisible():
    t.hideturtle()

print("Process END: " + str(datetime.now()))
print("Please close graphics window to end program.")

turtle.mainloop()
