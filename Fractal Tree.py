import turtle

def draw_branch(branch_length, t):
    if branch_length > 5:
        t.forward(branch_length)
        t.right(20)
        draw_branch(branch_length - 15, t)
        t.left(40)
        draw_branch(branch_length - 15, t)
        t.right(20)
        t.backward(branch_length)

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")

    fractal_tree = turtle.Turtle()
    fractal_tree.color("brown")
    fractal_tree.width(2)
    fractal_tree.left(90)
    fractal_tree.penup()
    fractal_tree.setpos(0, -200)
    fractal_tree.pendown()

    draw_branch(100, fractal_tree)

    screen.exitonclick()

if __name__ == "__main__":
    main()
