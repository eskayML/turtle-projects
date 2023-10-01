import turtle as t
import random

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def small_circle():
    """
    Draw a small circle
    """
    t.hideturtle()
    t.colormode(255)
    t.color(random_color())
    t.filling()
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    
def starting_point():  
    """
    starting point setup
    """
    t.penup()
    # t.hideturtle()
    t.setheading(225)
    t.forward(300)
    t.setheading(0)

def images():
    t.speed('fastest')
    number_of_dots = 100
    for dot_count in range(1,number_of_dots+1):
        t.colormode(255)
        t.dot(20,random_color())
        t.forward(50)
        if dot_count % 10 == 0:
            t.setheading(90)
            t.forward(50)
            t.setheading(180)
            t.forward(500)
            t.setheading(0)
            
starting_point()
images()
t.hideturtle()

screen = t.Screen()
screen.exitonclick()