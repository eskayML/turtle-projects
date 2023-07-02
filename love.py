from turtle import *

# Set up turtle environment
bgcolor('#9fa')
color('red')
shape('turtle')
title('First turtle program')
shapesize(10, 10)
fd(0)
shapesize(9, 9)
fd(0)
shapesize(8, 8)
fd(0)


# Draw a shape
begin_fill()
left(50)
forward(150)
circle(80, 180)
right(100)
circle(80, 180)
forward(150)
forward(41)
end_fill()


# Draw another shape
bgcolor('orange')
pencolor('white')
width(4)
backward(50)
right(90)
forward(30)
up()
forward(25)
down()

circle(20)
up()
forward(50)
down()

# Draw another shape
bgcolor('#222')
circle(13, -270)
left(90)
forward(26)
up()
right(90)
forward(200)

# Ending statement
bgcolor('pink')
done()
