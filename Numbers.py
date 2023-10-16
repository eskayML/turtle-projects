import turtle

screen = turtle.Screen()
t = turtle.Turtle()

# Screen setup
screen.setup(720, 600)
screen.bgcolor('black')

# Set up the color set and pen properties
t.pensize(7)
t.penup()
t.setpos(-300, 120)
t.pendown()
t.pencolor('purple')

# Functions for different digits
def nine(d):
    point = t.position()
    t.fd(d)
    t.rt(90)
    t.fd(d*2)
    pt = t.pos()
    t.bk(d)
    t.rt(90)
    t.fd(d)
    t.rt(90)
    t.fd(d)
    t.pu()
    t.goto(pt)
    t.pd()
    t.rt(90)
    t.bk(d)
    t.pu()
    t.goto(point)
    t.pd()
    t.setheading(0)
    
def eight(d):
    point = t.pos()
    t.fd(d)
    t.rt(90)
    t.fd(d*2)
    for i in range(3):
        t.rt(90)
        t.fd(d)
    t.bk(d)
    t.lt(90)
    t.fd(d)
    t.pu()
    t.goto(point)
    t.pd()
    t.setheading(0)

def seven(d):
    point = t.pos()
    t.fd(d)
    t.rt(90)
    t.fd(d*2)
    t.bk(d*2)
    t.lt(90)
    t.bk(d)
    t.pu()
    t.goto(point)
    t.pd()
    t.setheading(0)

def six(d):
    point = t.pos()
    t.fd(d)
    t.bk(d)
    t.rt(90)
    t.fd(d*2)
    for i in range(3):
        t.lt(90)
        t.fd(d)
    t.rt(90)
    t.fd(d)
    t.pu()
    t.goto(point)
    t.pd()
    t.setheading(0)

def five(d):
    point = t.pos()
    t.fd(d)
    t.bk(d)
    t.rt(90)
    t.fd(d)
    t.lt(90)
    t.fd(d)
    for i in range(2):
        t.rt(90)
        t.fd(d)
    t.pu()
    t.goto(point)
    t.pd()
    t.setheading(0)

def four(d):
    point = t.pos()
    t.rt(90)
    t.fd(d)
    for i in range(2):
        t.lt(90)
        t.fd(d)
    t.bk(d * 2)
    t.pu()
    t.goto(point)
    t.pd()
    t.setheading(0)

def three(d):
    point = t.pos()
    for i in range(2):
        t.fd(d)
        t.rt(90)
    t.fd(d)
    for i in range(2):
        t.bk(d)
        t.rt(90)
    t.bk(d)
    t.pu()
    t.goto(point)
    t.pd()
    t.setheading(0)

def two(d):
    point = t.pos()
    t.fd(d)
    t.rt(90)
    t.fd(d)
    t.lt(90)
    for i in range(2):
        t.bk(d)
        t.lt(90)
    t.bk(d)
    t.pu()
    t.goto(point)
    t.pd()
    t.setheading(0)

def one(d):
    point = t.pos()
    t.pu()
    t.fd(d)
    t.pd()
    t.rt(90)
    t.fd(d*2)
    t.pu()
    t.goto(point)
    t.pd()
    t.setheading(0)

def zero(d):
    point = t.pos()
    t.fd(d)
    t.rt(90)
    t.fd(d*2)
    t.rt(90)
    t.fd(d)
    t.rt(90)
    t.fd(d*2)
    t.pu()
    t.goto(point)
    t.pd()
    t.setheading(0)
    
num = int(input("enter the number: "))
num = str(num)
d = 50

for n in num:
    if (n=='1'):
        one(d)
    if (n=='2'):
        two(d)
    if (n=='3'):
        three(d)
    if (n=='4'):
        four(d)
    if (n=='5'):
        five(d)
    if (n=='6'):
        six(d)
    if (n=='7'):
        seven(d)
    if (n=='8'):
        eight(d)
    if (n=='9'):
        nine(d)
    if (n=='0'):
        zero(d)
    t.pu()
    t.fd(75)
    t.pd()

# Exit Turtle
t.hideturtle()
screen.exitonclick()
# turtle.bye()
# t.done()
