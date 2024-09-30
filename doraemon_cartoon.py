import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("white")

# Function to draw a filled circle
def draw_circle(radius, color):
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Function to draw a filled rectangle
def draw_rectangle(width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

# Function to draw Doraemon's face outline (big circle)
def draw_face():
    t.penup()
    t.goto(0, -200)
    t.pendown()
    t.pensize(3)
    draw_circle(200, "skyblue")  # Doraemon's blue head

# Function to draw Doraemon's white face
def draw_white_face():
    t.penup()
    t.goto(0, -150)
    t.pendown()
    draw_circle(150, "white")  # White inner face

# Function to draw Doraemon's eyes
def draw_eyes():
    t.penup()
    t.goto(-60, 50)
    t.pendown()
    draw_circle(30, "white")  # Left eye
    t.penup()
    t.goto(60, 50)
    t.pendown()
    draw_circle(30, "white")  # Right eye
    
    t.penup()
    t.goto(-60, 65)
    t.pendown()
    draw_circle(10, "black")  # Left pupil
    t.penup()
    t.goto(60, 65)
    t.pendown()
    draw_circle(10, "black")  # Right pupil

    # Adding blue eye highlights
    t.penup()
    t.goto(-55, 75)
    t.pendown()
    draw_circle(3, "blue")
    
    t.penup()
    t.goto(65, 75)
    t.pendown()
    draw_circle(3, "blue")

# Function to draw Doraemon's nose
def draw_nose():
    t.penup()
    t.goto(0, 30)
    t.pendown()
    draw_circle(20, "red")  # Nose

# Function to draw Doraemon's mouth
def draw_mouth():
    t.penup()
    t.goto(-70, -10)
    t.pendown()
    t.setheading(-60)
    t.circle(80, 120)  # Smile
    t.penup()
    t.goto(-70, -10)
    t.pendown()
    t.setheading(-60)

# Function to draw Doraemon's whiskers
def draw_whiskers():
    positions = [(-80, 0), (-80, -20), (-80, 20), (80, 0), (80, -20), (80, 20)]
    for x, y in positions:
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.setheading(0)
        if x < 0:  # Left whiskers
            t.forward(50)
        else:  # Right whiskers
            t.backward(50)

def draw_bell():
    t.penup()
    t.goto(0, -230)  
    t.pendown()
    draw_circle(30, "yellow") 

    t.penup()
    t.goto(0, -200)
    t.pendown()
    t.pensize(2)
    t.circle(10)  # Bell inner circle

# Drawing Doraemon Face step by step
draw_face()
draw_white_face()
draw_eyes()
draw_nose()
draw_mouth()
draw_whiskers()
draw_bell()

# Hide the turtle
t.hideturtle()

# Finish
turtle.done()
