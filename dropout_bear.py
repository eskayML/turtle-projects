import turtle 

turtle.colormode(255)

window = turtle.Screen()


def draw_head():
    """Draws the main head shape of Dropout Bear."""
    t.penup()
    t.goto(150, -100)
    t.pendown()
    t.color("black", "saddlebrown")
    t.begin_fill()

    # Top curved part
    t.setheading(60)  
    for _ in range(2):
        t.circle(190, 120)  
    
    # Bottom curve
    t.setheading(-30)  
    t.circle(329, 60)

    t.end_fill()




def draw_ears():
    """Draws the ears of Dropout Bear."""
    t.penup()
    t.goto(-150, 100)  # Left ear position
    t.pendown()
    t.color("black", "saddlebrown")
    t.begin_fill()
    t.circle(60)
    t.end_fill()

    t.penup()
    t.goto(-150, 110) # Left inner ear position
    t.pendown()
    t.color("black", "tan")
    t.begin_fill()
    t.circle(50)
    t.end_fill()

    t.penup()
    t.goto(100, 100)  # Right ear position
    t.pendown()
    t.color("black", "saddlebrown")
    t.begin_fill()
    t.circle(60)
    t.end_fill()

    t.penup()
    t.goto(100, 110) #Right inner ear position
    t.pendown()
    t.color("black", "tan")
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    

def draw_eyes():
    """Draws the eyes of Dropout Bear."""
    """Left eyes """
    #main pupil
    t.penup()
    t.goto(-110, 0)  # Left eye
    t.pendown()
    t.color( "black", "white")
    t.begin_fill()
    t.setheading(50)  # Face right
    for _ in range(2):
        t.circle(100, 60)  # Top curve
        t.circle(26, 120)  # Side curve
    t.end_fill()

    #burgundy outline
    t.penup()
    t.goto(-113, 10)  # Left eye
    t.pendown()
    t.color((52,22,12))
    t.begin_fill()
    t.setheading(50)  # Face right
    for _ in range(2):
        t.circle(90, 60)  # Top curve
        t.circle(20, 120)  # Side curve
    t.end_fill()

    #pink iris
    t.penup()
    t.goto(-113, 10)  # Left eye
    t.pendown()
    t.color((223,37,110))
    t.begin_fill()
    t.setheading(50)  # Face right
    for _ in range(2):
        t.circle(80, 60)  # Top curve
        t.circle(20, 120)  # Side curve
    t.end_fill()

    #gray pupil
    t.penup()
    t.goto(-120, 40)  # Left eye
    t.pendown()
    t.color((166,132,148))
    t.begin_fill()
    t.setheading(60)  # Face right
    for _ in range(2):
        t.circle(20, 60)  # Top curve
        t.circle(5, 120)  # Side curve
    t.end_fill()

    #pink pupil thing
    t.penup()
    t.goto(-115, 8.2)  # Left eye
    t.pendown()
    t.color((255,227,232))
    t.begin_fill()
    t.setheading(60)  # Face right
    for _ in range(2):
        t.circle(20, 60)  # Top curve
        t.circle(5, 120)  # Side curve
    t.end_fill()

    #yellow something on iris
    t.penup()
    t.goto(-125, 58)  # Left eye
    t.pendown()
    t.color((215,180,0))
    t.begin_fill()
    t.setheading(45)  # Face right
    for _ in range(2):
        t.circle(51, 60)  # Top curve
        t.circle(4, 120)  # Side curve
    t.end_fill()


    """Right Eye"""


    t.penup()
    t.goto(120, 5)  # Right eye
    t.pendown()
    t.color( "black", "white")
    t.begin_fill()
    t.setheading(70)  # Face left
    for _ in range(2):
        t.circle(100, 60)  # Top curve
        t.circle(25, 120)  # Side curve
    t.end_fill()

    #bluish teal outline
    t.penup()
    t.goto(115, 10) # right eye
    t.pendown()
    t.color((76,130,130))
    t.begin_fill()
    t.setheading(70)  # Face left
    for _ in range(2):
        t.circle(92, 60)  # Top curve
        t.circle(20, 120)  # Side curve
    t.end_fill()

    #black iris
    t.penup()
    t.goto(115, 10)  # right eye
    t.pendown()
    t.color((0,0,0))
    t.begin_fill()
    t.setheading(70)  # Face right
    for _ in range(2):
        t.circle(80, 60)  # Top curve
        t.circle(20, 120)  # Side curve
    t.end_fill()

    #grayish pinkish pupil
    t.penup()
    t.goto(100, 40)  # right eye
    t.pendown()
    t.color((223,176,158))
    t.begin_fill()
    t.setheading(70)  # Face right
    for _ in range(2):
        t.circle(20, 60)  # Top curve
        t.circle(5, 120)  # Side curve
    t.end_fill()

    #yellowish pupil
    t.penup()
    t.goto(113, 5)  # right eye
    t.pendown()
    t.color((225,221,98))
    t.begin_fill()
    t.setheading(60)  # Face right
    for _ in range(2):
        t.circle(20, 60)  # Top curve
        t.circle(5, 120)  # Side curve
    t.end_fill()

    #pink something on iris
    t.penup()
    t.goto(91, 58)  # Left eye
    t.pendown()
    t.color((239,129,140))
    t.begin_fill()
    t.setheading(72)  # Face right
    for _ in range(2):
        t.circle(47, 60)  # Top curve
        t.circle(4, 120)  # Side curve
    t.end_fill()


def draw_mouth_nose():
    """Draws the snout and nose."""
    #t.showturtle()
    t.penup() 
    t.goto(-10, 0)
    t.pendown()
    t.setheading(-180)
    t.color("black", (219,170,130))
    t.begin_fill()
    t.circle(90, 100)
    t.setheading(320)
    t.circle(120, 45)
    t.forward(2)


    t.penup() 
    t.goto(-10, 0)
    t.pendown()
    t.setheading(0)
    t.circle(-90, 100)
    t.setheading(-140)  
    t.circle(-120, 45)
 
    t.end_fill()
    
    t.penup()
    t.begin_fill()

    t.color("black", (79,64,45))
    t.goto(-0, -20)
    t.setheading(150)
    t.pendown()
    for _ in range(2):
        t.circle(20, 60)  
        t.circle(5, 120) 
    t.end_fill()


    
    
    

""" 
Did my best to draw kanye west's dropout bear
 but it came out more like a dropout
   mouse instead"""
    
# Initialize Turtle
t = turtle.Turtle()
t.speed(20)
turtle.bgcolor("purple")
t.hideturtle()
# Draw the bear step by step
draw_ears()
draw_head()
draw_eyes()
draw_mouth_nose()


window.exitonclick()