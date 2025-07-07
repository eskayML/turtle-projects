import turtle


FLAG_WIDTH = 600
FLAG_HEIGHT = 300
STRIPE_HEIGHT = FLAG_HEIGHT // 3
CHAKRA_RADIUS = 24

screen = turtle.Screen()
screen.title("Indian Flag 🇮🇳")
screen.bgcolor("white")


def draw_stripe(color, y_start):
    pen = turtle.Turtle()
    pen.speed(0)
    pen.penup()
    pen.goto(-FLAG_WIDTH // 2, y_start)
    pen.pendown()
    pen.color(color)
    pen.begin_fill()
    for _ in range(2):
        pen.forward(FLAG_WIDTH)
        pen.right(90)
        pen.forward(STRIPE_HEIGHT)
        pen.right(90)
    pen.end_fill()
    pen.hideturtle()

def draw_chakra():
    chakra = turtle.Turtle()
    chakra.speed(0)
    chakra.penup()
    chakra.goto(0, -STRIPE_HEIGHT//2 - CHAKRA_RADIUS) 
    chakra.setheading(0)
    chakra.pendown()
    chakra.color("blue")
    chakra.width(4)
    

    chakra.circle(CHAKRA_RADIUS)
    

    chakra.penup()
    chakra.goto(0, -STRIPE_HEIGHT//2)
    chakra.setheading(0)
    chakra.pendown()

    for _ in range(24):
        chakra.forward(CHAKRA_RADIUS)
        chakra.backward(CHAKRA_RADIUS)
        chakra.left(15)
    
    chakra.hideturtle()

draw_stripe("orange", STRIPE_HEIGHT)

draw_stripe("white", 0)
draw_stripe("green", -STRIPE_HEIGHT)

draw_chakra()

turtle.done()
