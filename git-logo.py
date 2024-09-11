import turtle as pen

#This turtle example graphic displays the git logo and does so completely in sequential order
#one could modify this to use functions allowing for code reuse to create the various shapes  


#turtle set up
pen.speed(10)
# '#f1502f' hex code for git logo color 
pen.pencolor("#f1502f")
pen.pensize("5")

#turtle starting location
pen.penup()
pen.goto(10,-200)
pen.left(45)


#Square with rounded edges
pen.pendown()
pen.fillcolor("#f1502f")
pen.begin_fill()
for i in range(2):
    pen.forward(250)
    pen.circle(30,90)
    pen.forward(250)
    pen.circle(30,90)
pen.end_fill()

#set up fill color for interior shapes
pen.penup()
pen.color("white")
pen.fillcolor("white")

#first node
pen.goto(13,-105)
pen.pendown()
pen.begin_fill()
pen.circle(30)
pen.end_fill()

#second node
pen.penup()
pen.goto(100,-20)
pen.pendown()
pen.begin_fill()
pen.circle(30)
pen.end_fill()

#third node
pen.penup()
pen.goto(15,60)
pen.pendown()
pen.begin_fill()
pen.circle(30)
pen.end_fill()

#diagonal line 
pen.penup()
pen.goto(60,1)
pen.pendown()
pen.begin_fill()
#creates and fills a rectange to conect the two nodes
for i in range(2):
    pen.forward(25)
    pen.left(90)
    pen.forward(230)
    pen.left(90)
pen.end_fill()


#virtical line
pen.penup()
pen.right(45)
pen.goto(-20,-90)
pen.pendown()
pen.begin_fill()
#creates and fills a rectange to conect the two nodes
for i in range(2):
    pen.forward(25)
    pen.left(90)
    pen.forward(180)
    pen.left(90)
pen.end_fill()
