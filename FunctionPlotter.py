from math import *
import turtle as t

"""
Title:  Function Plotter
Author: Aanjishnu Bhattacharyya

This program plots general mathematical functions. 
The default viewport is the smallest size such that
it can fit a unit circle.

* The Origin And Scaling is accepted as input from the user.
* The function must be a single variabled expression which returns
    a real number as output. The unknown variable name must be (x).
    The function should also ideally be continuous in the viewport range.

* The samples input tells the script how many points it should consider,
    the number which is accepted as input is raised to the power of 2 and
    that is the number of samples that will be sampled.

Cool Example:
    Function: cos(x)
    Origin:   0 0
    Scale:    6.3 1.5
    Samples:  6
"""

Function = None
Origin = None
Scale = None
Sample = 0

Points = None

def accept_input():
    print('Function Plotter')
    print('****************')
    print('NOTE: Please check out the file for more information on how to use the script.\n')

    # Accepting a function
    global Function

    try:
        text = input('Enter Function: ')
        Function = eval('lambda x: ' + text)
        Function(0)    # making sure that the function is fine
    except Exception:
        return False

    # Accepting Origin and Scale
    global Origin, Scale

    try:
        text = input('Enter Origin of plot [<real number> <real number>]: ')
        Origin = tuple(map(float, filter(None, text.split(' '))))

        if(len(Origin) != 2):
            return False

        text = input('Enter X-Scale Y-Scale of plot [<real number> <real number>]: ')
        Scale = tuple(map(float, filter(None, text.split(' '))))

        if(len(Scale) != 2):
            return False

    except Exception:
        return False

    # Accepting Sample Count
    global Sample

    try:
        text = input('Enter number of samples [<whole number>]: ')
        Sample = int(text)

        if(Sample <= 0):
            return False

    except Exception:
        return False

    return True

# Undefined points are not handled properly
def compute_points():
    global Points
    Points = [] 

    ss = 2 ** Sample - 1
    startx = -Scale[0] + Origin[0]
    dx = 2 * Scale[0] / ss

    for i in range(0, ss + 1):
        Points.append((startx, Function(startx)))
        startx += dx

def draw_picture():
    t.title('Plotter')
    t.resizemode('noresize')
    t.setworldcoordinates(Origin[0] - Scale[0], Origin[1] - Scale[1], Origin[0] + Scale[0], Origin[1] + Scale[1])

    t.clearscreen()

    # Drawing Axis
    t.penup()
    t.setpos(Origin[0], Origin[1] - Scale[1])
    t.pendown()
    t.setheading(270)
    t.stamp()
    t.goto(Origin[0], Origin[1] + Scale[1])
    t.setheading(90)
    t.stamp()

    t.penup()
    t.setpos(Origin[0] - Scale[0], Origin[1])
    t.pendown()
    t.setheading(180)
    t.stamp()
    t.goto(Origin[0] + Scale[0], Origin[1])
    t.setheading(0)
    t.stamp()

    t.penup()
    t.goto(Origin[0], Origin[1])
    t.pendown()
    t.dot(5, 'red')
    t.write(f"({Origin[0]}, {Origin[1]})", False)

    # Drawing the Points

    t.penup()
    t.goto(Points[0][0], Points[0][1])
    t.pendown()

    k = 0
    for i in Points:
        t.goto(i[0], i[1])
        t.dot(5, 'blue')
        print(f"({round(i[0], 3)}, {round(i[1], 3)})")

        if k % 5 == 0:
            t.write(f"({round(i[0], 3)}, {round(i[1], 3)})", False)

        t.penup()
        t.goto(Origin[0], i[1])
        t.pendown()
        t.dot(5, 'green')

        t.penup()
        t.goto(i[0], Origin[1])
        t.pendown()
        t.dot(5, 'green')

        t.penup()
        t.setpos(i[0], i[1])
        t.pendown()
        k += 1

    t.exitonclick()

def main():
    if(not accept_input()):
        print('Invalid Input')
    else:
        # print(Function, *Origin, *Scale, Sample)
        print('Points Sampled (from left to right): ')
        compute_points()
        draw_picture()

if __name__ == '__main__':
    main()
