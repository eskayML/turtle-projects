import turtle
import math

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
t.color("cyan")

# Draw network pattern
for angle in range(0, 360, 15):
    t.setheading(angle)
    for distance in range(0, 200, 20):
        t.forward(distance)
        t.backward(distance)

turtle.done()