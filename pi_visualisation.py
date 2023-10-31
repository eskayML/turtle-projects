import turtle

# Set up the Turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a Turtle object for drawing the pie chart
pie_chart = turtle.Turtle()
pie_chart.speed(1)  # Set the drawing speed (you can adjust it)

# Function to draw a pie slice
def draw_slice(percent, color):
    pie_chart.fillcolor(color)
    pie_chart.begin_fill()
    pie_chart.circle(100, percent * 3.6)  # 3.6 degrees per 1% of the pie
    pie_chart.goto(0, 0)
    pie_chart.end_fill()

# Data for the pie chart
slices = [(40, "red"), (30, "green"), (20, "blue")]  # (percentage, color)

# Draw the pie chart
start_angle = 0
for percent, color in slices:
    draw_slice(percent, color)
    start_angle += percent * 3.6

# Close the drawing
pie_chart.hideturtle()
screen.exitonclick()
