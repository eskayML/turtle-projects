import turtle
import time

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Simple Analog Clock")
screen.setup(500, 500)

# Create turtle for drawing
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

def draw_clock_face():
    # Draw clock circle
    t.penup()
    t.goto(0, -200)
    t.pendown()
    t.color("white")
    t.pensize(3)
    t.circle(200)
    
    # Draw numbers
    t.penup()
    for i in range(1, 13):
        angle = i * 30
        x = 160 * turtle.sin(turtle.radians(angle))
        y = 160 * turtle.cos(turtle.radians(angle)) - 10
        t.goto(x, y)
        t.write(str(i), align="center", font=("Arial", 16, "normal"))

def draw_hand(angle, length, width, color):
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.setheading(90 - angle)
    t.color(color)
    t.pensize(width)
    t.forward(length)

def update_clock():
    # Clear previous hands
    t.clear()
    draw_clock_face()
    
    # Get current time
    current_time = time.localtime()
    hours = current_time.tm_hour
    minutes = current_time.tm_min
    seconds = current_time.tm_sec
    
    # Calculate angles
    second_angle = seconds * 6
    minute_angle = minutes * 6 + seconds * 0.1
    hour_angle = (hours % 12) * 30 + minutes * 0.5
    
    # Draw hands
    draw_hand(hour_angle, 80, 6, "blue")    # Hour hand
    draw_hand(minute_angle, 120, 4, "green") # Minute hand  
    draw_hand(second_angle, 150, 2, "red")   # Second hand
    
    # Draw center dot
    t.penup()
    t.goto(0, 0)
    t.dot(10, "white")
    
    # Update every second
    screen.ontimer(update_clock, 1000)

# Start the clock
update_clock()

# Keep window open
screen.exitonclick()