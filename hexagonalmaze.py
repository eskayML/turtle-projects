import turtle as t
import random
import math

width, height = 800, 800
# screen setup
background = t.Screen()
background.bgcolor("black")
background.setup(width, height)
background.title("Hexagonal Maze Generator")

# maze pen
maze = t.Turtle()
maze.pensize(3)
maze.speed("fastest")
maze.color("red")


class hexagon:
    def __init__(self, row, col):
        self.side1wall = True
        self.side2wall = True
        self.side3wall = True
        self.side4wall = True
        self.side5wall = True
        self.side6wall = True

        self.visited = False
        self.row = row
        self.col = col
        self.neighbours = None

        Hspacing = math.sqrt(3) * side
        Vspacing = 3 / 4 * heightofhex

        self.y = -Vspacing * row + Vspacing * rows / 2
        self.x = Hspacing * col - Hspacing * cols / 2
        self.x += Hspacing / 2 if row % 2 == 0 else 0

    def next(self):
        while True:
            if len(self.neighbours) > 0:
                side = random.choice(list(self.neighbours.keys()))
                nexttriangle = self.neighbours[side]
                del self.neighbours[side]
                # checking if it is visited or not
                if nexttriangle.visited:
                    continue
                self.remove_wall(side)
                nexttriangle.remove_wall((side + 2) % 6 + 1)
                return nexttriangle
            return False

    def remove_wall(self, side):
        if side == 1:
            self.side1wall = False
        elif side == 2:
            self.side2wall = False
        elif side == 3:
            self.side3wall = False
        if side == 4:
            self.side4wall = False
        elif side == 5:
            self.side5wall = False
        elif side == 6:
            self.side6wall = False

    def draw(self, side):
        maze.penup()
        maze.goto(self.x, self.y + side)
        maze.pendown()
        maze.left(210)

        if self.side1wall:
            maze.pendown()
        else:
            maze.penup()
        maze.forward(side)
        maze.left(60)
        if self.side2wall:
            maze.pendown()
        else:
            maze.penup()
        maze.forward(side)
        maze.left(60)
        if self.side3wall:
            maze.pendown()
        else:
            maze.penup()
        maze.forward(side)
        maze.left(60)
        if self.side4wall:
            maze.pendown()
        else:
            maze.penup()
        maze.forward(side)
        maze.left(60)
        if self.side5wall:
            maze.pendown()
        else:
            maze.penup()
        maze.forward(side)
        maze.left(60)
        if self.side6wall:
            maze.pendown()
        else:
            maze.penup()
        maze.forward(side)
        maze.right(150)

    def getNeighbours(self):
        neighbours = {}
        iseven = (self.row) % 2
        i, j = self.row, self.col
        if i - 1 >= 0:
            # left top
            if j - iseven >= 0:
                neighbours[1] = grid[i - 1][j - iseven]
            # right top
            if j + 1 - iseven < cols:
                neighbours[6] = grid[i - 1][j + 1 - iseven]
        if i + 1 < rows:
            # bottom left
            if j - iseven >= 0:
                neighbours[3] = grid[i + 1][j - iseven]
            # bottom right
            if j + 1 - iseven < cols:
                neighbours[4] = grid[i + 1][j + 1 - iseven]
        # right
        if j + 1 < cols:
            neighbours[5] = grid[i][j + 1]
        # left
        if j - 1 >= 0:
            neighbours[2] = grid[i][j - 1]
        return neighbours


rows, cols = 10, 10
side = 35
heightofhex = side * 2
widthofhex = side * (3**0.5)
stack = []

# init the trainagular grid
grid = []
for i in range(rows):
    temp = []
    for j in range(cols):
        temp.append(hexagon(i, j))
    grid.append(temp)

# calculate neighbours
for i in range(len(grid)):
    for j in range(len(grid[i])):
        grid[i][j].neighbours = grid[i][j].getNeighbours()


# dfs maze generator
def mazegenerator(start=grid[0][0]):
    current = start
    # maze.penup()
    # maze.goto(current.x, current.y)
    # maze.pendown()
    while True:
        current.visited = True
        # maze.goto(current.x, current.y)
        nextside = current.next()
        if nextside:
            stack.append(current)
            current = nextside
        elif len(stack) > 0:
            current = stack.pop()
        else:
            return


mazegenerator()

# draw the final maze
for i in range(len(grid)):
    for j in range(len(grid[i])):
        grid[i][j].draw(side - maze.pensize())

maze.hideturtle()
background.exitonclick()
