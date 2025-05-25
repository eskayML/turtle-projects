from turtle import Turtle, Screen

LETTER_HEIGHT = 100
LETTER_HALF_HEIGHT = LETTER_HEIGHT // 2
LETTER_QUARTER_HEIGHT = LETTER_HEIGHT // 4
LETTER_WIDTH = 40
LETTER_HALF_WIDTH = LETTER_WIDTH // 2
LETTER_DISTANCE = 20

def setup(turtle: Turtle, screen: Screen):
    turtle.goto(x=-250, y=100)
    turtle.pencolor("orange")
    screen.bgcolor("black")
    screen.title("Hello World!")
    turtle.pensize(10)


def draw(turtle: Turtle):
    _draw_sentence("hello world!", turtle)

def _draw_exclamation_mark(turtle: Turtle):
    turtle.right(90)
    turtle.forward(LETTER_HALF_HEIGHT + LETTER_QUARTER_HEIGHT)
    turtle.penup()
    turtle.forward(LETTER_QUARTER_HEIGHT)
    turtle.pendown()
    turtle.dot()
    turtle.penup()
    turtle.back(LETTER_HEIGHT)
    turtle.left(90)
    turtle.pendown()

def _draw_d(turtle: Turtle):
    turtle.penup()
    turtle.right(90)
    turtle.forward(LETTER_HALF_HEIGHT)
    turtle.pendown()
    turtle.left(90)
    _draw_rectangle(turtle, LETTER_HALF_HEIGHT, LETTER_HALF_WIDTH)
    turtle.forward(LETTER_HALF_WIDTH)
    turtle.left(90)
    turtle.forward(LETTER_HALF_HEIGHT)
    turtle.right(90)

def _draw_r(turtle: Turtle):
    turtle.penup()
    turtle.right(90)
    turtle.forward(LETTER_HALF_HEIGHT)
    turtle.pendown()
    turtle.forward(LETTER_HALF_HEIGHT)
    turtle.back(LETTER_HALF_HEIGHT)
    turtle.left(90)
    turtle.forward(LETTER_HALF_WIDTH)
    turtle.penup()
    turtle.left(90)
    turtle.forward(LETTER_HALF_HEIGHT)
    turtle.right(90)

def _prepare_next_word(turtle: Turtle):
    _prepare_next_letter(turtle)
    _prepare_next_letter(turtle)

def _draw_w(turtle: Turtle):
    turtle.right(90)
    turtle.forward(LETTER_HEIGHT)
    turtle.left(135)
    turtle.forward(LETTER_HALF_WIDTH)
    turtle.right(90)
    turtle.forward(LETTER_HALF_WIDTH)
    turtle.left(135)
    turtle.forward(LETTER_HEIGHT)
    turtle.right(90)




def _draw_o(turtle: Turtle):
    turtle.penup()
    turtle.right(90)
    turtle.forward(LETTER_HALF_HEIGHT)
    turtle.left(90)
    turtle.pendown()
    _draw_rectangle(turtle, LETTER_HALF_HEIGHT, LETTER_HALF_WIDTH)
    turtle.forward(LETTER_HALF_WIDTH)
    turtle.left(90)
    turtle.penup()
    turtle.forward(LETTER_HALF_HEIGHT)
    turtle.pendown()
    turtle.right(90)

def _draw_l(turtle: Turtle):
    turtle.right(90)
    turtle.forward(LETTER_HEIGHT)
    turtle.back(LETTER_HEIGHT)
    turtle.left(90)

def _draw_e(turtle: Turtle):
    turtle.penup()
    turtle.right(90)
    turtle.forward(LETTER_HALF_HEIGHT)
    turtle.pendown()
    turtle.forward(LETTER_HALF_HEIGHT)
    turtle.left(90)
    turtle.forward(LETTER_HALF_WIDTH)
    turtle.backward(LETTER_HALF_WIDTH)
    turtle.left(90)
    turtle.forward(LETTER_HALF_HEIGHT)
    turtle.pendown()
    turtle.right(90)
    _draw_rectangle(turtle, LETTER_QUARTER_HEIGHT, LETTER_HALF_WIDTH),
    turtle.penup()
    turtle.left(90)
    turtle.forward(LETTER_HALF_HEIGHT)
    turtle.right(90)
    turtle.forward(LETTER_HALF_WIDTH)



def _draw_h(turtle: Turtle):
    turtle.right(90)
    turtle.fd(LETTER_HEIGHT)
    turtle.left(180)
    turtle.fd(LETTER_HALF_HEIGHT)
    turtle.right(90)
    turtle.fd(LETTER_WIDTH)
    turtle.left(90)
    turtle.fd(LETTER_HALF_HEIGHT)
    turtle.right(180)
    turtle.fd(LETTER_HEIGHT)
    turtle.left(180)
    turtle.fd(LETTER_HEIGHT)
    turtle.right(90)

def _prepare_next_letter(turtle: Turtle):
    turtle.penup()
    turtle.fd(LETTER_DISTANCE)
    turtle.pendown()

def _draw_rectangle(turtle: Turtle, height: int, width: int):
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)

def _draw_letter(letter: str, turtle: Turtle):
    LETTER_DRAWERS = {
        "!": _draw_exclamation_mark,
        "d": _draw_d,
        "r": _draw_r,
        "w": _draw_w,
        "o": _draw_o,
        "l": _draw_l,
        "e": _draw_e,
        "h": _draw_h
    }
    LETTER_DRAWERS[letter](turtle)

def _draw_word(word: str, turtle: Turtle):
    for let in word:
        _prepare_next_letter(turtle)
        _draw_letter(let, turtle)

def _draw_sentence(sentence: str, turtle: Turtle):
    words = sentence.split()
    for word in words:
        _prepare_next_word(turtle)
        _draw_word(word, turtle)

def hello_world():
    turtle = Turtle()
    screen = Screen()
    setup(turtle=turtle, screen=screen)
    draw(turtle=turtle)
    turtle.screen.mainloop()

if __name__ == "__main__":
    hello_world()