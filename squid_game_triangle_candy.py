import turtle

def draw_circle():
    # Draw the outer circle of the candy with a thick border.
    turtle.penup()
    turtle.goto(0, -150)
    turtle.pendown()
    turtle.pensize(3)  
    turtle.color("#5a430c", "#c8a646")
    turtle.begin_fill()
    turtle.circle(150)
    turtle.end_fill()

def draw_outer_circle():
    # Draw the container for the candy.
    turtle.penup()
    turtle.goto(0, -180)
    turtle.pendown()
    turtle.pensize(6)  
    turtle.color("#a7c3c7", "#bfcacc")
    turtle.begin_fill()
    turtle.circle(180)
    turtle.end_fill()

def draw_triangle():
    # Draw a larger triangle in the center of the candy with a thick border.
    turtle.penup()
    turtle.goto(-80, -50)
    turtle.pendown()
    turtle.pensize(5)  
    turtle.color("#5a430c", "#cfb659") 
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(160)
        turtle.left(120)
    turtle.end_fill()

def draw_needle():
    # Draw a needle inside the candy container.
    turtle.penup()
    turtle.goto(-70, -70)
    turtle.pendown()
    turtle.pensize(5)
    turtle.color("gray")  
    turtle.setheading(45)  
    turtle.forward(220) 
    turtle.backward(220)  
    turtle.setheading(135)
    turtle.forward(10) 
    turtle.backward(10)

def draw_candy():
    # Draw the complete candy.
    turtle.speed(3)
    turtle.hideturtle()
    draw_outer_circle()  
    draw_circle() 
    draw_triangle()  
    draw_needle()  

if __name__ == "__main__":
    screen = turtle.Screen()
    screen.bgcolor("#fffaf0")  
    draw_candy()
    screen.mainloop()