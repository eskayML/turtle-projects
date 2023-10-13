import turtle
import random

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Spiral with Changing Colors")

# Create a Turtle object for drawing
spiral = turtle.Turtle()
spiral.speed(0)
spiral.width(2)

# Function to draw the spiral with changing colors
def draw_spiral(angle, length, repetitions):
    for _ in range(repetitions):
        spiral.color(random.random(), random.random(), random.random())
        spiral.forward(length)
        spiral.right(angle)
        length += 5

# Function to clear the screen and reset the Turtle
def clear_screen():
    spiral.clear()
    spiral.penup()
    spiral.goto(0, 0)
    spiral.pendown()

# Create an animation loop
while True:
    draw_spiral(90, 50, 30)  # Change the parameters to create different patterns
    clear_screen()

# Close the program when the user clicks on the screen
wn.exitonclick()
