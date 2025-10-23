import turtle
import math

def setup_screen():
    """Set up the turtle screen with coordinates"""
    screen = turtle.Screen()
    screen.setup(1000, 700)
    screen.title("Math Function Plotter - Sine & Cosine Waves")
    screen.bgcolor("black")
    return screen

def draw_axes(pen):
    """Draw X and Y axes"""
    pen.color("white")
    pen.pensize(2)
    
    # Y-axis
    pen.penup()
    pen.goto(-450, 0)
    pen.pendown()
    pen.goto(450, 0)
    
    # X-axis
    pen.penup()
    pen.goto(0, -300)
    pen.pendown()
    pen.goto(0, 300)
    
    # Labels
    pen.penup()
    pen.goto(460, -20)
    pen.write("X", font=("Arial", 14, "normal"))
    pen.goto(-20, 310)
    pen.write("Y", font=("Arial", 14, "normal"))

def draw_ticks(pen):
    """Draw scale ticks on axes"""
    pen.color("gray")
    pen.pensize(1)
    
    # X-axis ticks
    for x in range(-400, 401, 50):
        pen.penup()
        pen.goto(x, -10)
        pen.pendown()
        pen.goto(x, 10)
        if x != 0:
            pen.penup()
            pen.goto(x-10, -30)
            pen.write(f"{x//50}π", font=("Arial", 10, "normal"))
    
    # Y-axis ticks
    for y in range(-250, 251, 50):
        pen.penup()
        pen.goto(-10, y)
        pen.pendown()
        pen.goto(10, y)
        if y != 0:
            pen.penup()
            pen.goto(20, y-10)
            pen.write(f"{y/50}", font=("Arial", 10, "normal"))

def plot_function(pen, func, color, label):
    """Plot a mathematical function"""
    pen.penup()
    pen.color(color)
    pen.pensize(2)
    
    # Move to first point
    x = -400
    y = func(x/50) * 50  # Scale factor
    pen.goto(x, y)
    pen.pendown()
    
    # Plot the function
    for x in range(-400, 401, 2):
        y = func(x/50) * 50  # Scale for better visualization
        pen.goto(x, y)
    
    # Add legend
    pen.penup()
    pen.goto(300, 250 - (len(label) * 20))
    pen.write(label, font=("Arial", 12, "normal"))

def sine_wave(x):
    """Sine function"""
    return math.sin(x)

def cosine_wave(x):
    """Cosine function"""
    return math.cos(x)

def tangent_wave(x):
    """Tangent function (with limits)"""
    try:
        return math.tan(x)
    except:
        return 0

def main():
    # Setup
    screen = setup_screen()
    pen = turtle.Turtle()
    pen.speed(0)
    pen.hideturtle()
    
    # Draw coordinate system
    draw_axes(pen)
    draw_ticks(pen)
    
    # Plot different functions
    plot_function(pen, sine_wave, "cyan", "sin(x) - Sine Wave")
    plot_function(pen, cosine_wave, "yellow", "cos(x) - Cosine Wave")
    plot_function(pen, tangent_wave, "magenta", "tan(x) - Tangent Wave")
    
    # Add title and instructions
    pen.penup()
    pen.goto(-200, 320)
    pen.color("green")
    pen.write("Math Function Plotter - Trigonometric Waves", font=("Arial", 16, "bold"))
    
    pen.goto(-200, -350)
    pen.color("white")
    pen.write("Functions: sin(x) = Cyan, cos(x) = Yellow, tan(x) = Magenta", font=("Arial", 12, "normal"))
    
    screen.exitonclick()

if __name__ == "__main__":
    main()