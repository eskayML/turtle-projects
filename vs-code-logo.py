from turtle import *
bgcolor('black')

# firstly, move the turtle to a very comfortable position to start from
up()
goto(-150,0)
down()
pencolor('#0c6cb0')
fillcolor('#0c6cb0')
begin_fill()
left(45)
fd(250)
right(60)
fd(50)
right(75)
fd(250)

# fillcolor('#467deb')
# begin_fill()
right(60)
fd(50)
right(75)
fd(250)

# first little circle
circle(-10,174)
fd(270)
# end_fill()


# fillcolor('#3f77e8')
# begin_fill()
back(60)
left(130)
fd(230)
# end_fill()


back(60)
left(128)
fd(210)
circle(-10,180)
end_fill()

up()
goto(-120,-200)
down()
pencolor('white')
write('Visual Studio Code', font=('Arial', 20, 'normal'))
done()
