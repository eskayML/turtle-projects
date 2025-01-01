import turtle
import time

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("Moving Car with Rotating Wheels")

# Create the turtle for drawing
t = turtle.Turtle()
t.hideturtle()
t.speed(0)

# Function to draw a rectangle
def draw_rectangle(x, y, width, height, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

# Function to draw a tree
def draw_tree(x, y):
    # Draw trunk
    draw_rectangle(x, y, 20, 40, "brown")
    # Draw leaves (centered above the trunk)
    t.penup()
    t.goto(x + 10, y + 40)  # Center of the leaves
    t.pendown()
    t.color("green")
    t.begin_fill()
    t.circle(30)  # Draw circular leaves
    t.end_fill()

# Draw the road
def draw_road():
    draw_rectangle(-300, -50, 600, 100, "gray")  # Road base
    # Dashed white line
    t.penup()
    t.color("white")
    t.goto(-300, -5)
    t.width(3)
    t.setheading(0)
    for _ in range(15):
        t.pendown()
        t.forward(20)
        t.penup()
        t.forward(20)

# Draw background elements
draw_road()
draw_tree(-200, 50)
draw_tree(100, 50)
draw_tree(250, 50)

# Create the turtle for the car body (a simple red rectangle)
car = turtle.Turtle()
car.penup()
car.shape("square")
car.color("red")
car.shapesize(stretch_wid=2, stretch_len=3)  # Car body proportions

# Create the turtle for the wheels
left_wheel = turtle.Turtle()
left_wheel.shape("circle")
left_wheel.color("black")
left_wheel.penup()

right_wheel = turtle.Turtle()
right_wheel.shape("circle")
right_wheel.color("black")
right_wheel.penup()

# Function to rotate the wheels
def rotate_wheels():
    left_wheel.setheading(left_wheel.heading() + 10)  # Rotate left wheel
    right_wheel.setheading(right_wheel.heading() + 10)  # Rotate right wheel

# Initial positions for the car and wheels (starting from the left side)
car.goto(-260, -20)  
left_wheel.goto(-290, -40)  
right_wheel.goto(-230, -40)  

# Move the car with rotating wheels
for position in range(-260, 260, 5):  
    # Move car body
    car.goto(position, -20)  
    
    # Move wheels along with the car
    left_wheel.goto(position - 30, -40)  
    right_wheel.goto(position + 30, -40)  
    
    rotate_wheels()  # Rotate the wheels as the car moves
    time.sleep(0.05)  # Pause for smooth motion

# Keep the window open
turtle.done()
