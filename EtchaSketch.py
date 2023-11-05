from turtle import Turtle, Screen

eas = Turtle()
screen = Screen()


def move_forward():
    eas.forward(50)


def turn_right():
    eas.rt(10)


def turn_left():
    eas.lt(10)


def move_backward():
    eas.backward(50)


def clear_screen():
    eas.clear()
    eas.penup()
    eas.home()
    eas.pendown()


screen.listen()

screen.onkey(move_forward, 'w')
screen.onkey(move_backward, 's')
screen.onkey(turn_left, 'a')
screen.onkey(turn_right, 'd')
screen.onkey(clear_screen, 'space')

screen.exitonclick()
