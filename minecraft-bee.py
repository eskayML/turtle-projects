from turtle import *
import time
t = Turtle()

# Made by lvxq37-2
# I intentionally kept functions beside their calls so it is clear where the code is used

t.speed(10000)

# Setting up: repositioning bee
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
t.color('#FFEE5F')
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
t.color('#FFD75E')
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
    t.color('#7A3D13')
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

stripes(1)
t.penup()
t.forward(2*side)

t.pendown()
stripes(1)
t.penup()
t.forward(2*side)

t.pendown()
stripes(2)
t.penup()

# Repositioning turtle
t.left(180)
t.penup()
t.forward(2*side)
t.pendown()

# Legs
def legs(length):
    t.begin_fill()
    t.forward(side)
    t.left(60)
    t.forward(side*(length-1))
    t.left(60)
    t.forward(side)
    t.left(120)
    t.forward(side*length)
    t.left(120)
    t.end_fill()

legs(2)
t.forward(side*2)
legs(2)
t.forward(side*2)
legs(1)

#Repositioning
t.penup()
t.forward(side)
t.right(120)
t.forward(side)
t.right(60)

# Left side eye
# Black Section
t.color('black')
t.pendown()
t.begin_fill()
t.forward(side)
t.left(60)
t.forward(3*side)
t.left(120)
t.forward(side)
t.right(60)
t.forward(side)
t.left(120)
t.forward(side)
t.right(120)
t.forward(side)
t.left(120)
t.forward(2*side)
t.end_fill()

# Colored section of left eye
t.left(180)
t.forward(2*side)
t.color('#30C8BE')
t.begin_fill()
for i in range(2):
    for value in [120, 60]:
        t.forward(side)
        t.right(value)
t.end_fill()

#Repositioning
t.forward(side)
t.penup()
t.left(60)
t.forward(side)

# Left side antenna
t.right(120)
t.color('black')
t.pendown()
t.begin_fill()
t.forward(side)
t.right(60)
t.forward(side)
t.left(120)
t.forward(side)
t.left(60)
t.forward(side)
t.left(60)
t.forward(side)
t.end_fill()

t.right(120)
t.begin_fill()
t.forward(side)
t.left(120)
t.forward(2*side)
t.left(60)
t.forward(side)
t.end_fill()

# Right side eye
t.begin_fill()
t.forward(2*side)
t.right(120)
t.forward(2*side)
t.right(60)
t.forward(3*side)
t.right(120)
t.forward(side)
t.right(60)
t.forward(side)
t.end_fill()

# Repositioning
t.left(180)
t.forward(2*side)

# Right side antenna
t.begin_fill()
t.left(120)
t.forward(2*side)
t.right(120)
t.forward(side)
t.right(60)
t.forward(2*side)
for i in range(3):
    t.right(60)
    t.forward(side)
t.end_fill()

# Colored part of right eye
t.left(60)
t.color('#30C8BE')
t.begin_fill()
for i in range(2):
    for value in [60, 120]:
        t.forward(side)
        t.left(value)
t.end_fill()

# Outline
t.right(120)
t.color('black')
t.forward(side)
t.right(60)
t.forward(3*side)
for i in range(2):
    t.right(60)
    t.forward(10*side)
    t.right(60)
    t.forward(7*side)
    t.right(60)
    t.forward(7*side)
t.right(120)
t.forward(7*side)
t.right(60)
t.forward(7*side)
t.right(180)
t.forward(7*side)
t.right(60)
t.forward(10*side)

t.hideturtle()

done()