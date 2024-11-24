import turtle

def draw_petal(t, radius, angle):

    t.begin_fill()

    for x in range(2):
        t.circle(radius, angle) 
        t.left(180 - angle)

    t.end_fill()

def draw_sunflower(t, num_petals):
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Sunflower")

    t.speed(0)
    t.color("gold")

    petal_radius = 120
    petal_angle = 60 

    for x in range(num_petals):
        draw_petal(t, petal_radius, petal_angle)
        t.right(360 / num_petals) 

    center_size = 50

    t.penup()
    t.goto(0, center_size * -1)
    t.pendown()

    t.pencolor("#FF8C00") 
    t.pensize(3) 
    t.fillcolor("brown") 
    t.begin_fill()
    t.circle(center_size) 
    t.end_fill()

    turtle.done()

if __name__ == "__main__":
    t = turtle.Turtle()
    num_petals = 18
    draw_sunflower(t, num_petals)  

