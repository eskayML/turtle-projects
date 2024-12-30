import turtle
import math

def draw_react_logo():
    screen = turtle.Screen()
    screen.bgcolor('#20232a') 
    screen.title('React Logo')
    
    orbits = turtle.Turtle()
    orbits.speed(0)
    orbits.pensize(4)
    orbits.hideturtle()
    orbits.color('#61DAFB')
    
    nucleus = turtle.Turtle()
    nucleus.speed(0)
    nucleus.hideturtle()
    
    def draw_orbital(t, tilt):
        t.penup()
        t.goto(0, -60)
        t.setheading(tilt)
        t.pendown()
        
        for i in range(360):
            angle = math.radians(i)
            x = math.sin(angle) * 120
            y = math.cos(angle) * 60
            t.goto(x * math.cos(math.radians(tilt)) - y * math.sin(math.radians(tilt)),
                  x * math.sin(math.radians(tilt)) + y * math.cos(math.radians(tilt)))
    
    angles = [0, 120, 240]
    for angle in angles:
        draw_orbital(orbits, angle)
    
    nucleus.penup()
    nucleus.goto(0, -20)
    nucleus.color('#61DAFB')
    nucleus.begin_fill()
    nucleus.circle(20)
    nucleus.end_fill()
    
    screen.exitonclick()

draw_react_logo()
