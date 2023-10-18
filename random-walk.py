import turtle as t
import random

tortugita = t.Turtle()

colours = [
  "DarkOrchid2",
  "DeepSkyBlue",
  "firebrick2",
  "LawnGreen",
  "orchid2",
  "SpringGreen",
  "wheat",
  "gold"
]
directions = [0, 90, 180, 270]
tortugita.pensize(15)
tortugita.speed("fastest")

# How many times the turtle will move
for _ in range(400):
  # Select a random color each time the turtle makes a step
  tortugita.color(random.choice(colours))
  # How far the turtle moved
  tortugita.forward(35)
  # Make the turtle going in a random direction
  tortugita.setheading(random.choice(directions))