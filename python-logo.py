from turtle import Screen, Turtle

def curved_box(t, sides):
    for _ in range(sides):
        t.circle(90, extent=90)
        t.forward(120)

    t.circle(90, extent=90)

def snake(t, color):
    t.backward(16)
    t.left(90)
    t.forward(16)
    t.right(90)

    t.fillcolor(color)

    t.begin_fill()
    t.forward(64)
    curved_box(t, 2)
    t.forward(44)
    t.left(90)
    t.forward(152)
    t.right(90)
    t.forward(16)
    t.right(90)
    t.forward(204)
    curved_box(t, 1)
    t.forward(44)
    t.left(90)
    t.forward(60)
    t.circle(-90, extent=90)
    t.forward(64)
    t.end_fill()

    t.backward(86)
    t.left(90)
    t.forward(224)
    t.dot(48, 'white')
    t.backward(224)
    t.right(90)
    t.forward(86)

screen = Screen()

turtle = Turtle()
turtle.penup()

snake(turtle, '#3774A8')
turtle.left(180)
snake(turtle, '#F6D646')

screen.exitonclick()