import turtle
import time

# Create the turtle screen and turtle
screen = turtle.Screen()
tp = turtle.Turtle()

# Set up the screen size and background color
screen.setup(420, 320)
screen.bgcolor('black')

# Set up the color set and pen properties
colour_set = ['red', 'green', 'blue', 'yellow', 'purple']
tp.pensize(4)
tp.penup()
tp.setpos(-90, 30)
tp.pendown()

# Draw the shape using different colors
for i in range(5):
    tp.pencolor(colour_set[i])
    tp.forward(200)
    tp.right(144)

# Move to a new position and hide the turtle
tp.penup()
tp.setpos(80, -140)
tp.pendown()
tp.ht()
tp.done()
