import turtle
import sys
from datetime import datetime


t = turtle.Turtle()

i = 200

print("\nProcess START: " + str(datetime.now()))

for x in range(i):
    t.forward(x)
    t.right(90)

if t.isvisible():
    t.hideturtle()

print("Process END: " + str(datetime.now()))
    
print("Please close graphics window to end program.")

turtle.mainloop()
