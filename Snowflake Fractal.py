import turtle

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Snowflake Fractal")

# Create a Turtle object for drawing the snowflake
snowflake = turtle.Turtle()
snowflake.speed(0)
snowflake.color("blue")
snowflake.penup()
snowflake.goto(-200, 0)
snowflake.pendown()

# Function to draw a Koch snowflake
def draw_koch_snowflake(length, depth):
    if depth == 0:
        snowflake.forward(length)
    else:
        length /= 3.0
        draw_koch_snowflake(length, depth - 1)
        snowflake.left(60)
        draw_koch_snowflake(length, depth - 1)
        snowflake.right(120)
        draw_koch_snowflake(length, depth - 1)
        snowflake.left(60)
        draw_koch_snowflake(length, depth - 1)

# Function to create a snowflake fractal
def create_snowflake(length, depth):
    for _ in range(3):
        draw_koch_snowflake(length, depth)
        snowflake.right(120)

# Create a snowflake fractal
create_snowflake(400, 4)

# Close the program when the user clicks on the screen
wn.exitonclick()

