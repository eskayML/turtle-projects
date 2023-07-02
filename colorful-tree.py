import turtle as t

size = int(input("Size: ")) #50 to 100 is recommended

# Set up the turtle window
t.bgcolor("black")
t.pensize(2)
t.color("green")
t.left(90)
t.backward(size)
t.speed(0)
t.hideturtle()
t.shape("turtle")

# Recursive function to draw the tree
def tree(i):
    if i < 10:
        return
    else:
        # Draw the trunk
        t.forward(i)
        t.color("orange")
        t.circle(2)
        t.color("brown")

        # Draw the left branch
        t.left(30)
        tree(3 * i / 4)

        # Draw the right branch
        t.right(60)
        tree(3 * i / 4)

        # Return to the trunk
        t.left(30)
        t.backward(i)

# Call the tree function with the given size
tree(size)

# Finish drawing
t.done()
