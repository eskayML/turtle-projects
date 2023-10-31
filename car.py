import turtle as t

# Create a turtle screen
screen = t.Screen()
screen.bgcolor("white")

# Create a turtle object for the car
car = t.Turtle()
car.shape("square")
car.color("blue")

# Function to draw a rectangle
def draw_rectangle(width, height, color):
    car.color(color)
    car.begin_fill()
    for _ in range(2):
        car.forward(width)
        car.left(90)
        car.forward(height)
        car.left(90)
    car.end_fill()

# Function to draw a circle
def draw_circle(radius, color):
    car.penup()
    car.color(color)
    car.pendown()
    car.begin_fill()
    car.circle(radius)
    car.end_fill()
    car.penup()
    car.pendown()

# Draw the car body
draw_rectangle(200, 50, "blue")

# Draw the windows
car.penup()
car.goto(50, 0)
car.pendown()
draw_rectangle(100, 30, "black")

# Draw the roof
car.penup()
car.goto(30, 50)
car.pendown()
draw_rectangle(140, 20, "blue")

# Draw the wheels
car.penup()
car.goto(40, -10)
car.pendown()
draw_circle(20, "black")

car.penup()
car.goto(160, -10)
car.pendown()
draw_circle(20, "black")

# Position the car
car.penup()
car.goto(0, -10)
car.pendown()

# Hide the turtle
car.hideturtle()

# Keep the window open
t.done()
