import turtle as tur
tur.bgcolor("#0a3445")
tur.penup()
tur.goto(0,20)
tur.pendown()
tur.speed(1)
tur.pencolor("white")
 
def circle(size):
    tur.pensize(15)
    # tur.fillcolor('white')
    tur.circle(size)
    tur.penup()

circle(70)

tur.goto(28,160)
tur.pendown()
tur.left(90)
tur.forward(60)
for i in range(90):
        tur.left(2)
        tur.forward(1)
tur.forward(60)
tur.penup()
tur.goto(-20,90)
tur.begin_fill()
tur.fillcolor('white')
circle(20)
tur.end_fill()
tur.penup()


tur.goto(-55,35)
tur.pendown()
tur.right(25)

tur.forward(140)
tur.penup()
tur.forward(60)
tur.pendown()
tur.forward(150)

tur.left(30)
tur.forward(50)
tur.left(120)
tur.forward(50)

tur.left(30)
tur.forward(151)
tur.penup()
tur.forward(60)
tur.pendown()
tur.forward(139)

tur.penup()
tur.left(-65)
tur.forward(20)
tur.pendown()

tur.right(65)
tur.forward(135)
tur.penup()
tur.forward(55)
tur.pendown()
tur.forward(160)
tur.left(30)
tur.forward(50)


tur.left(120)
tur.forward(50)
tur.left(30)
tur.forward(350)

tur.penup()

tur.backward(280)
tur.pendown()
tur.right(90)

tur.pensize(1)
tur.forward(8)
tur.pencolor("#3DDC84")
tur.begin_fill()
for i in range(89):
        tur.left(2)
        tur.forward(4)
tur.fillcolor("#3DDC84")
tur.end_fill()

tur.pencolor("white")

tur.pensize(15)
tur.penup()
tur.left(90)
tur.forward(60)
tur.left(90)
tur.forward(55)
tur.pendown()

circle(1)


tur.left(-90)
tur.forward(100)

tur.pendown()
circle(1)

tur.left(-90)
tur.forward(110)
tur.pencolor("#3DDC84")
tur.left(-88)
tur.forward(20)

tur.left(90)

tur.pendown()

tur.pencolor("white")

for i in range(37):
        tur.right(1.2)
        tur.forward(5)

tur.penup()
for i in range(11):
        tur.right(1.2)
        tur.forward(5)

tur.pendown()
for i in range(22):
        tur.right(1.2)
        tur.forward(5)

tur.left(-90)
tur.forward(50)
tur.left(-90)

for i in range(16):
        tur.left(1.5)
        tur.forward(5)

tur.penup()
for i in range(11):
        tur.left(1.5)
        tur.forward(5)
tur.pendown()

for i in range(28):
        tur.left(1.5)
        tur.forward(5)

        

tur.pencolor("#3DDC84")
tur.penup()
tur.forward(110)
tur.left(30)
tur.forward(58)
tur.pensize(5)
tur.pendown()
tur.forward(60)
tur.pensize(15)


tur.penup()
tur.backward(120)
tur.left(-120)
tur.forward(50)

tur.left(60)
tur.forward(60)
tur.pensize(5)
tur.pendown()
tur.forward(60)
tur.pensize(15)


tur.hideturtle()

tur.done()