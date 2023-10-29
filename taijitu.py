from turtle import *

fillcolor('black')
begin_fill()
circle(100, 180)
end_fill()
circle(100, 180)

# Draw smaller black semicircle
left(180)
penup()
goto(0, 100)
pendown()
begin_fill()
circle(50, 180)
end_fill()

# Draw smaller white semicircle
penup()
goto(0, 100)
pendown()
fillcolor('white')
begin_fill()
circle(50, 180)
end_fill()

# Draw smaller circles
penup()
goto(0, 50 + 20)
begin_fill()
circle(20)
end_fill()

fillcolor('black')
goto(0, 2 * (100 - 20))
begin_fill()
circle(20)
end_fill()

# Exit on click feature
exitonclick()
