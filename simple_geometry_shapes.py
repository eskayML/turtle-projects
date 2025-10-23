import turtle
import math

# Setup screen
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("Simple Geometry Shapes")

# Create turtle
t = turtle.Turtle()
t.speed(2)
t.pensize(3)

# Draw Circle
t.penup()
t.goto(-200, 0)
t.pendown()
t.color("red")

radius = 50
t.circle(radius)
area_circle = 3.14 * radius * radius

t.penup()
t.goto(-200, -70)
t.write(f"Circle Area: {area_circle:.1f}", font=("Arial", 12, "normal"))

# Draw Square
t.penup()
t.goto(0, 0)
t.pendown()
t.color("blue")

side = 80
for i in range(4):
    t.forward(side)
    t.left(90)

area_square = side * side

t.penup()
t.goto(0, -70)
t.write(f"Square Area: {area_square}", font=("Arial", 12, "normal"))

# Draw Triangle
t.penup()
t.goto(150, 0)
t.pendown()
t.color("green")

base = 100
height = 80

t.forward(base)
t.left(135)
t.forward(height)
t.left(90)
t.forward(height)

area_triangle = 0.5 * base * height

t.penup()
t.goto(150, -70)
t.write(f"Triangle Area: {area_triangle}", font=("Arial", 12, "normal"))

# Draw Rectangle
t.penup()
t.goto(-100, -150)
t.pendown()
t.color("orange")

width = 120
height_rect = 60

for i in range(2):
    t.forward(width)
    t.left(90)
    t.forward(height_rect)
    t.left(90)

area_rectangle = width * height_rect

t.penup()
t.goto(-100, -230)
t.write(f"Rectangle Area: {area_rectangle}", font=("Arial", 12, "normal"))

t.penup()
t.goto(-200, -260)
t.color("black")
t.write("Click to exit", font=("Arial", 12, "normal"))

screen.exitonclick()