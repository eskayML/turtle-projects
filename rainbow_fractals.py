from turtle import Turtle, done
import argparse
import random
from multiprocessing import Process
import colorsys

t = Turtle()

FIGURES = ("snowflake", "triangle", "carpet", "cross", "cross2")
col = random.randint(0, 259)
COLOR_STEP = 10

def main(figure, depth):
	t.shape("turtle")
	t.speed(0) # Max speed
	color()

	if figure == None:
		figure = random.choice(FIGURES)
		print(f"No figure specified, randomly choosing {figure}")


	if figure == "snowflake":
		snowflake(depth, 300);
	elif figure == "triangle":
		triangle(depth, 300)
	elif figure == "carpet":
		carpet(depth, 300)
	elif figure == "cross":
		cross(depth, 300)
	elif figure == "cross2":
		cross2(depth, 300)

	done()

# Use hsv to iterate over color palette
# https://www.alanzucconi.com/2015/09/30/colour-sorting/
def color():
	global col
	r, g, b = colorsys.hsv_to_rgb(col/360.0,1,1)
	t.color(r, g, b)
	col = (col + COLOR_STEP + 360) % 360


# Kock snowflake
def snowflake(n, length):
	# Go to position
	t.penup()
	t.goto(-length/2, 0)
	t.left(60)
	t.pendown()

	# Draw triangle
	snowflake_edge(n, length/3)
	t.right(120)
	snowflake_edge(n, length/3)
	t.right(120)
	snowflake_edge(n, length/3)


def snowflake_edge(n, l):
	# End case: just draw a straight line
	if n == 1:
		color()
		t.forward(3 * l)
	# Recursive call
	elif n > 1:
		snowflake_edge(n - 1, l / 3)
		t.left(60)
		snowflake_edge(n - 1, l / 3)
		t.right(120)
		snowflake_edge(n - 1, l / 3)
		t.left(60)
		snowflake_edge(n - 1, l / 3)
	# Wrong input
	else:
		print(f"n must be > 0, got {n}")


def triangle(n, length):
	# Go to position
	t.penup()
	t.goto(-length/2, 0)
	t.left(60)
	t.pendown()

	triangle_r(n, length)

def triangle_r(n, l):
	# End case: just fill a triangle
	if n == 1:
		color()
		t.begin_fill()
		for _ in range(3):
			t.forward(l)
			t.right(120)
		t.end_fill()
	# Recursive call
	elif n > 1:
		for _ in range(3):
			triangle_r(n-1, l/2)
			t.penup()
			t.forward(l)
			t.right(120)
			t.pendown()
	# Wrong input
	else:
		print(f"n must be > 0, got {n}")


# Sierpinski carpet
def carpet(n, length):
	# Go to position
	t.penup()
	t.goto(-length/2, length/2)
	t.pendown()

	carpet_square(n, length)

def carpet_square(n, l):
	# End case: fill a black square
	if n == 1:
		color()
		t.begin_fill()
		for _ in range(4):
			t.forward(l)
			t.right(90)
		t.end_fill()
	# Recursive call
	elif n > 1:
		for _ in range(4):
			carpet_square(n-1, l/3)
			t.penup()
			t.forward(l/3)
			t.pendown()
			carpet_square(n-1, l/3)
			t.penup()
			t.forward(l/3)
			t.forward(l/3)
			t.right(90)
			t.pendown()
	# Wrong input
	else:
		print(f"n must be > 0, got {n}")


# Vicsek cross (diagonal)
def cross(n, length):
	# Go to position
	t.penup()
	t.goto(-length/2, length/2)
	t.pendown()

	cross_square(n, length)

def cross_square(n, l):
	# End case: fill a black square
	if n == 1:
		color()
		t.begin_fill()
		for _ in range(4):
			t.forward(l)
			t.right(90)
		t.end_fill()
	# Recursive call
	elif n > 1:
		# 4 external squares
		for _ in range(4):
			cross_square(n-1, l/3)
			t.penup()
			t.forward(l)
			t.right(90)
			t.pendown()
		# Central square
		t.penup()
		t.forward(l/3)
		t.right(90)
		t.forward(l/3)
		t.left(90)
		t.pendown()
		cross_square(n-1,l/3)
		# Go back to initial position
		t.penup()
		t.left(90)
		t.forward(l/3)
		t.left(90)
		t.forward(l/3)
		t.right(180)
	# Wrong input
	else:
		print(f"n must be > 0, got {n}")


# Vicsek cross (vertical)
def cross2(n, length):
	# Go to position
	t.penup()
	t.goto(-length/2, length/2)
	t.pendown()

	cross2_square(n, length)

def cross2_square(n, l):
	# End case: fill a black square
	if n == 1:
		color()
		t.begin_fill()
		for _ in range(4):
			t.forward(l)
			t.right(90)
		t.end_fill()
	# Recursive call
	elif n > 1:
		# 4 external squares
		for _ in range(4):
			t.penup()
			t.forward(l/3)
			t.pendown()
			cross2_square(n-1, l/3)
			t.penup()
			t.forward(l/3)
			t.forward(l/3)
			t.right(90)
			t.pendown()
		# Central square
		t.penup()
		t.forward(l/3)
		t.right(90)
		t.forward(l/3)
		t.left(90)
		t.pendown()
		cross2_square(n-1,l/3)
		# Go back to initial position
		t.penup()
		t.left(90)
		t.forward(l/3)
		t.left(90)
		t.forward(l/3)
		t.right(180)
	# Wrong input
	else:
		print(f"n must be > 0, got {n}")

if __name__ == '__main__':
	# Allow user input
	parser = argparse.ArgumentParser()
	parser.add_argument('--figure', type=str, default=None, choices=FIGURES, help=f'The fractal figure to draw {FIGURES}')
	parser.add_argument('--depth', type=int, default=5, help='The number of recursive calls')
	args = parser.parse_args()
	
	# Ensure depth is valid
	if args.depth < 1:
		print(f"Depth must be >= 1, got {args.depth}")
		args.depth = 5
	
	# Main run
	main(args.figure, args.depth)