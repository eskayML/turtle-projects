import turtle
import math

screen = turtle.Screen()
screen.title('Diamond Shape')
screen.setup(1000,1000)
screen.setworldcoordinates(-1000,-1000,1000,1000)
turtle.speed(0)
turtle.hideturtle()

def diamond(x,y, width, height, angle):
    turtle.up()
    turtle.color('red')
    turtle.goto(x,y-height/2)
    d = ((width/2)**2 + (height/2)**2)**0.5
    radius = d*0.5/math.sin(math.radians(angle/2))
    turtle.down()
    turtle.begin_fill()
    turtle.seth(turtle.towards(x-width/2,y)-angle/2)
    turtle.circle(radius, angle,20)
    turtle.seth(turtle.towards(x,y+height/2)-angle/2)
    turtle.circle(radius, angle,20)
    turtle.seth(turtle.towards(x+width/2,y)-angle/2)
    turtle.circle(radius, angle,20)
    turtle.seth(turtle.towards(x,y-height/2)-angle/2)
    turtle.circle(radius, angle,20)
    turtle.end_fill()    

diamond(0,0,1200,1600,20)