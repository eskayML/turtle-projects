import turtle
import random

def draw_christmas_tree():
    screen = turtle.Screen()
    screen.bgcolor("navy")
    screen.title("Christmas Tree with Decorations")
    
    t = turtle.Turtle()
    t.speed(0)
    t.pensize(2)
    
    # Tree trunk
    t.penup()
    t.goto(0, -200)
    t.pendown()
    t.color("brown")
    t.begin_fill()
    for _ in range(2):
        t.forward(30)
        t.left(90)
        t.forward(50)
        t.left(90)
    t.end_fill()
    
    # Tree layers
    tree_colors = ["dark green", "forest green", "green"]
    layer_sizes = [180, 140, 100, 60]
    
    for i, size in enumerate(layer_sizes):
        t.penup()
        t.goto(-size/2, -150 + i*50)
        t.pendown()
        t.color(tree_colors[i % len(tree_colors)])
        t.begin_fill()
        t.goto(0, -100 + i*50 + size/2)
        t.goto(size/2, -150 + i*50)
        t.goto(-size/2, -150 + i*50)
        t.end_fill()
    
    # Decorations (ornaments)
    ornament_colors = ["red", "gold", "blue", "purple", "orange"]
    ornament_positions = [
        (-40, -50), (30, -30), (-20, 0), (25, 20), 
        (-35, 40), (15, 60), (-10, 80)
    ]
    
    for pos in ornament_positions:
        t.penup()
        t.goto(pos)
        t.pendown()
        t.color(random.choice(ornament_colors))
        t.begin_fill()
        t.circle(8)
        t.end_fill()
    
    # Star on top
    t.penup()
    t.goto(-15, 120)
    t.pendown()
    t.color("gold")
    t.begin_fill()
    for _ in range(5):
        t.forward(30)
        t.right(144)
    t.end_fill()
    
    t.hideturtle()
    screen.exitonclick()

if __name__ == "__main__":
    draw_christmas_tree()