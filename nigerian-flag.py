from turtle import *
import time
t = Turtle()

t.speed(8000)

bgcolor('black')
t.color('white')
t.pencolor('white')
t.pensize(2)
title("Nigerian Flag ")
t.up()
t.goto(-200,50)
t.down()
t.left(90)

flag_width , flag_height = 300, 150

# t.pencolor('white')
t.fillcolor('green')
t.begin_fill()
for i in range(2):
    t.forward(flag_height)
    t.right(90)
    t.forward(flag_width)
    t.right(90)
t.end_fill()

t.up()

t.forward(flag_height)
t.right(90)
t.forward(flag_width/3)
t.down()

# now drawing the white part of the flag
t.fillcolor('white')
t.begin_fill()
for i in range(2):
    t.forward(flag_width/3)
    t.right(90)
    t.forward(flag_height)
    t.right(90)
t.end_fill()

t.up()
t.forward(flag_width * 2/3)
t.down()

# start drawing the flagpole 
t.pensize(1)
t.fillcolor("#222")
t.begin_fill()
t.right(90)
t.circle(10, -180)
t.backward(flag_height * 3)
t.circle(10, -180)
t.right(180)
t.forward(flag_height *3)
t.end_fill()

t.backward(80)

for i in range(8):
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(3)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.backward(3)
    
    
t.backward(150)
for i in range(8):
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(3)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.backward(3)
    
t.up()
t.goto(-220,-180)
t.down()

t.pencolor('white')
t.pensize(19)
t.write("THE NIGERIAN FLAG", font= ('Algerian', 22, 'bold'), align='left')

t.up()
t.backward(20)
t.right(90)
t.fd(100)
t.left(90)
t.backward(30)
t.shapesize(2,2)
t.color('white')
t.down()

shape_dict = ['arrow', 'turtle', 'circle', 'square', 'triangle', 'classic']

t.speed(.1)
while True:
    for shape in shape_dict:
        t.shape(shape)
        time.sleep(.4)
        
        
done()
