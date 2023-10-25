import turtle as t
import random

width, height = 800, 800
# screen setup
background = t.Screen()
background.bgcolor("black")
background.setup(width, height)
background.title("Maze Generator")

# maze pen
maze = t.Turtle()
maze.pensize(5)
maze.speed("fastest")
maze.color("red")


class triangle:
    def __init__(self, row, col):
        self.side1wall = True
        self.side2wall = True
        self.side3wall = True
        self.visited = False
        self.row = row
        self.col = col
        self.total_width = side * (row // 2 + 1)
        if row % 2 == 0:
            self.x = (col * side) + (side // 2) - self.total_width // 2
            self.y = (
                -((row + 1) // 2) * heightoftriangle
                + (heightoftriangle // 2)
                + height // 4
            )
        else:
            self.x = (col * side) + (side // 2) - self.total_width // 2
            self.y = (
                -((row + 1) // 2 - 2) * heightoftriangle
                + (heightoftriangle // 2)
                + height // 4
            )
        self.neighbours = None
        self.yoff = 0

    def next(self):
        while True:
            if len(self.neighbours) > 0:
                side = random.choice(list(self.neighbours.keys()))
                nexttriangle = self.neighbours[side]
                del self.neighbours[side]
                # checking if it is visited or not
                if nexttriangle.visited: continue
                nexttriangle.remove_wall(side)
                self.remove_wall(side)
                return nexttriangle
            return False

    def remove_wall(self, s):
        if s == "side1":
            self.side1wall = False
        elif s == "side2":
            self.side2wall = False
        elif s == "side3":
            self.side3wall = False

    def getNeighbours(self):
        i, j = self.row, self.col
        neighbours = {}
        if i % 2 == 0:
            # above 2 and below 1
            if i - 1 >= 0:
                if j - 1 >= 0:
                    neighbours["side1"] = grid[i - 1][j - 1]
                if j < len(grid[i - 1]):
                    neighbours["side2"] = grid[i - 1][j]
            # below
            if i + 1 < len(grid):
                neighbours["side3"] = grid[i + 1][j]
        else:
            # below 2 and above 1
            if i + 1 < len(grid):
                neighbours["side2"] = grid[i + 1][j]
                neighbours["side1"] = grid[i + 1][j + 1]
            # above
            if i - 1 >= 0:
                neighbours["side3"] = grid[i - 1][j]

        return neighbours

    def draw(self):
        maze.penup()
        maze.goto(self.x, self.y)
        if self.row % 2 != 0:
            # Upright triangle
            maze.goto(maze.xcor() - (0.5 * side), maze.ycor() - (0.5 * heightoftriangle))
            maze.setheading(0)  # Set the direction to upright
            maze.pendown()

            if not self.side2wall:maze.penup()
            else:maze.pendown()
            maze.right(60)
            maze.forward(side)
            maze.left(120)

            if not self.side1wall: maze.penup()
            else:maze.pendown()
            maze.forward(side)
            maze.left(120)

            if not self.side3wall:maze.penup()
            else:maze.pendown()
            maze.forward(side)
            maze.left(120)
            
        else:
            # Inverted triangle
            maze.goto(maze.xcor()- (0.5 * side), maze.ycor() + (0.5 * heightoftriangle))
            maze.setheading(0)  # Set the direction to upright
            maze.pendown()

            if not self.side1wall:maze.penup()
            else:maze.pendown()
            maze.left(60)
            maze.forward(side)
            maze.right(120)

            if not self.side2wall:maze.penup()
            else:maze.pendown()
            maze.forward(side)
            maze.right(120)

            if not self.side3wall:maze.penup()
            else:maze.pendown()
            maze.forward(side)
            maze.right(120)

rows = 30
side = 20
heightoftriangle = side * 0.5 * (3**0.5)
stack = []

# init the trainagular grid
grid = []
for i in range(2 * rows - 1):
    temp = []
    for j in range((i // 2) + 1):
        temp.append(triangle(i, j))
    grid.append(temp)

# calculate neighbours
for i in range(len(grid)):
    for j in range(len(grid[i])):
        grid[i][j].neighbours = grid[i][j].getNeighbours()

# dfs maze generator
def mazegenerator(start=grid[0][0]):
    current = start
    while True:
        current.visited = True
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
maze.speed("fastest")
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if i % 2 == 0:
            grid[i][j].draw()


background.exitonclick()
