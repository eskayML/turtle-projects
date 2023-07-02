from turtle import *

# Set the turtle speed and background color
speed(2)
bgcolor("black")

# Move to the starting position
penup()
goto(-50, 60)
pendown()

# Draw the filled shape
color("#00adef")
begin_fill()
goto(100, 100)
goto(100, -100)
goto(-50, -60)
goto(-50, 60)
end_fill()

# Draw the vertical line
color("black")
goto(15, 100)
color("black")
width(10)
goto(15, -100)

# Move to the horizontal line starting position
penup()
goto(100, 0)
pendown()

# Draw the horizontal line
goto(-100, 0)

done()
