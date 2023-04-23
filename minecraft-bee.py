from turtle import *
import time
t = Turtle()

t.speed(10000)

bgcolor('sky blue')
t.pensize(2)
title("Minecraft Bee")
t.up()
t.goto(0,-150)
t.down()
t.left(30)


side = 25
bee_w, bee_l = 7*side, 10*side      

# Main body fill: yellow
color = '#FFEE5F'
t.pencolor(color)
t.fillcolor(color)
t.begin_fill()
for i in range(2):
    t.forward(bee_l)
    t.left(60)
    t.forward(bee_w)
    t.left(60)#
    t.forward(bee_w)
    t.left(60)
t.end_fill()

# Pollen on lower body: tan
color = '#FFD75E'
t.pencolor(color)
t.fillcolor(color)
t.begin_fill()
for i in range(2):
    t.forward(bee_l)
    t.left(60)
    t.forward(side)
    t.left(120)
t.end_fill()

t.left(120)
t.begin_fill()
for i in range(2):
    t.forward(bee_w)
    t.right(60)
    t.forward(side)
    t.right(120)
t.end_fill()

# Stripes: brown
def stripes(thick):
    color = '#7A3D13'
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    t.forward(thick*side)
    t.left(60)
    t.forward(bee_w)
    t.left(60)
    t.forward(bee_w)
    t.left(60)
    t.forward(thick*side)
    t.left(120)
    t.forward(bee_w)
    t.right(60)
    t.forward(bee_w)
    t.left(120)
    t.end_fill()

t.right(120)
t.forward(4*side)

def switch(color):
    t.forward(side)
    t.pencolor(color)       # create colour swap function

stripes(1)
switch('#FFD75E')           # this is to stop the colors from overlapping
t.forward(side)

stripes(1)
switch('#FFD75E')
t.forward(side)

stripes(2)
switch('#FFD75E')
t.pencolor(color)



done()