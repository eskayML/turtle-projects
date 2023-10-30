from turtle import *

hideturtle()
speed(5)
width(1)

shape("circle")
bgcolor("black")
shapesize(2.7, 2.3, 5)

forward(226)
left(90)


def main_circle():
    color("#7289DA")
    begin_fill()
    circle(227, 360)
    end_fill()


def main_body():
    color("white")
    begin_fill()
    penup()
    goto(54, -80)
    pendown()
    right(150)
    forward(32)
    left(80)
    circle(350, 14)
    left(50)
    circle(249, 41)
    left(30)
    circle(225, 17)
    left(80)
    forward(18)
    right(85)
    circle(150, 26)
    right(80)
    forward(20)
    left(80)
    circle(225, 17)
    left(25)
    circle(249, 40)
    left(50)
    circle(310, 16)
    left(79)
    forward(32)
    left(100)
    forward(15)
    right(10)
    forward(15)
    right(120)
    forward(10)
    right(60)
    circle(150, 60)
    right(90)
    forward(7)
    right(90)
    forward(15)
    goto(54, -80)
    end_fill()
    

def eyes():
    color("#7289DA")
    penup()
    goto(48, -10)
    setheading(0)
    stamp()
    
    backward(97)
    stamp()
    

main_circle()
main_body()
eyes()

done()
