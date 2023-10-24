import turtle as t
import random
import math

# width and height of the screen
radius = 400
width, height = radius * 2 + 100, radius * 2 + 100
rings = 20
stack = []


class Segment:
    def __init__(self, level, cell_no):
        self.inner_wall = True
        self.right_wall = True
        self.visited = False
        self.level = level
        self.cell_no = cell_no

    def __str__(self):
        return f"level: {self.level}, cell_no: {self.cell_no}, inner_wall: {self.inner_wall}, right_wall: {self.right_wall}, visited: {self.visited}"

    def removewall(self, c):
        if self.level == c.level:
            if self.cell_no > c.cell_no:
                self.right_wall = False
            else:
                c.right_wall = False
        elif self.level > c.level:
            self.inner_wall = False
        else:
            c.inner_wall = False


# init the segment distribution: basically in what ring how many segment should be present
rings_cells = [[Segment(0, 1)]]
for ring in range(1, rings):
    level = ring + 1
    cells = 2 ** (int(math.log2(level)) + 3)
    rings_cells.append([Segment(ring, i) for i in range(cells)])
    # [[inner wall, right wall], [inner wall, right wall], ...]

# screen setup
background = t.Screen()
background.bgcolor("black")
background.setup(width, height, 0, 0)
background.title("Circular Maze Generator")


# maze pen
maze = t.Turtle()
maze.pensize(2)
maze.speed("fastest")
maze.color("red")


# get neighbours of current coordinate which are not visited
def getNeighbours(s):
    # for the center cell
    if s.level == 0:
        neighbours = []
        for cell in rings_cells[1]:
            if not cell.visited:
                neighbours.append(cell)
        return random.choice(neighbours) if len(neighbours) else False

    # for the rest of the cells
    neighbours = []
    count_of_cells = len(rings_cells[s.level])
    # right neighbour
    right_index = (s.cell_no + 1) % count_of_cells
    if not rings_cells[s.level][right_index].visited:
        neighbours.append(rings_cells[s.level][right_index])

    # left neighbour
    left_index = (s.cell_no - 1) % count_of_cells
    if not rings_cells[s.level][left_index].visited:
        neighbours.append(rings_cells[s.level][left_index])

    # inner neighbour
    if s.level - 1 > 0:
        count_of_innercells = len(rings_cells[s.level - 1])
        div = (
            1 if count_of_cells == count_of_innercells else 2.1
        )  # There are 1 inner cells for 2 cell
        innerN = rings_cells[s.level - 1][int(s.cell_no // div)]
        if not innerN.visited:
            neighbours.append(innerN)

    # outer neighbour
    if s.level + 1 < rings:
        count_of_outercells = len(rings_cells[s.level + 1])
        # There are two outer cells for one inner cell
        if count_of_cells != count_of_outercells:
            outerN1 = rings_cells[s.level + 1][s.cell_no * 2]
            outerN2 = rings_cells[s.level + 1][s.cell_no * 2 + 1]
            if not outerN1.visited:
                neighbours.append(outerN1)
            if not outerN2.visited:
                neighbours.append(outerN2)
        # There is one outer cell for one inner cell
        else:
            outerN = rings_cells[s.level + 1][s.cell_no]
            if not outerN.visited:
                neighbours.append(outerN)

    # choosing 1 neigbhour in random
    if len(neighbours) > 0:
        return random.choice(neighbours)


# maze generation algorithm
# step 1: mark the current cell as visited and get a list of its neighbours which are not visited
# step 2: if neighbour is available: append this coordinate to the stack
# step 3: if no neighbour is available: pop a cell from the stack and make it the current cell and repeat step 1
# step 4: if no neighbour and stack is empty: this means we have visited all the cells and the maze is generated
def mazegenerator():
    current = rings_cells[0][0]
    while True:
        current.visited = True
        next = getNeighbours(current)
        if next:
            next.removewall(current)
            stack.append(current)
            current = next
        elif len(stack) > 0:
            current = stack.pop()
        else:
            return


def coordinates(r, angle):
    x = r * math.cos(math.radians(angle))
    y = r * math.sin(math.radians(angle))
    maze.goto(x, y)


def drawmaze():
    for level, cells in enumerate(rings_cells[1:], 1):
        # maze.color("white" if level % 2 else "red")
        ring_w = (radius // rings)
        maze.penup()
        coordinates(level * ring_w, 0)
        maze.pendown()
        for cell_no, cell in enumerate(cells):
            angle_btw = 360 / len(cells)
            # right wall
            if cell.right_wall:
                coordinates((level + 1) * ring_w, cell_no * angle_btw)
                coordinates(level * ring_w, cell_no * angle_btw)
            # inner wall
            if not cell.inner_wall:
                maze.penup()
                coordinates(level * ring_w, (cell_no + 1) * angle_btw)
                maze.pendown()
            coordinates(level * ring_w, (cell_no + 1) * angle_btw)

    # last circle
    maze.penup()
    maze.goto(radius, 0)
    maze.pendown()
    maze.left(90)
    maze.circle(radius)

mazegenerator()
drawmaze()

background.exitonclick()
