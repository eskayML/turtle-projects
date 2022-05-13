#spirograph
from turtle import *


bgcolor('black')
colors = ['red','orange','yellow','green','blue','indigo','violet']
speed(1000)
for i in range(360):
    pencolor(colors[i%len(colors)])
    pensize(i/16)
    forward(i)
    right(61)


done()