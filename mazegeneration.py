import turtle as t
import random

# width and height of the screen
# you can change the width, height, rows, cols as you like
width, height = 800, 800 
rows, cols = 30, 30


cell_size = width // cols
stack = []

# screen setup
background = t.Screen()
background.bgcolor("black")
background.setup(width, height)
background.title("Maze Generator")


# maze pen
maze = t.Turtle()
maze.pensize(cell_size - 4)
maze.speed("fastest")
maze.color("white")

# style pen
pen2 = t.Turtle()
pen2.pensize(cell_size - 4)
pen2.speed("fastest")
pen2.color("red")


# make grid to keep track of visited cells
grid = [[False]*cols for _ in range(rows)]

# shifting the coordinates axis to the top left corner and scaling the grid according to the cell size
def coordinates(x, y):
    padding = 7
    grid_x = x * cell_size - width / 2 + cell_size / 2 + padding
    grid_y = - y * cell_size + height / 2 - cell_size / 2 - padding
    maze.goto(grid_x, grid_y)
    # style
    pen2.goto(grid_x, grid_y)

# get neighbours of current coordinate which are not visited
def getNeighbours(row, col):
    neighbours = []
    if row > 0 and not grid[row - 1][col]: neighbours.append((row - 1, col))
    if row < rows - 1 and not grid[row + 1][col]: neighbours.append((row + 1, col))
    if col > 0 and not grid[row][col - 1]: neighbours.append((row, col - 1))
    if col < cols - 1 and not grid[row][col + 1]: neighbours.append((row, col + 1))
    if len(neighbours) > 0:return random.choice(neighbours)
    else: return False


# maze generation algorithm
# step 1: mark the current cell as visited and get a list of its neighbours which are not visited
# step 2: if neighbour is available: append this coordinate to the stack
# step 3: if no neighbour is available: pop a cell from the stack and make it the current cell and repeat step 1
# step 4: if no neighbour and stack is empty: this means we have visited all the cells and the maze is generated

def mazegenerator(start=(0, 0)):
    current = start
    maze.penup()
    pen2.penup()
    coordinates(current[0], current[1])
    maze.pendown()
    pen2.pendown()
    while True:
        grid[current[0]][current[1]] = True
        next = getNeighbours(current[0], current[1])
        if next:
            stack.append(current)
            current = next
            coordinates(current[0], current[1])
        elif len(stack) > 0:
            current = stack.pop()
            coordinates(current[0], current[1])
        else:return

mazegenerator()

background.exitonclick()