import turtle
import heapq

# --- Configuration ---
GRID_WIDTH = 25  # Number of columns
GRID_HEIGHT = 25 # Number of rows
CELL_SIZE = 24
SPEED_FACTOR = 10 # Draw every 10th step. Higher = Faster

# Colors
COLOR_DEFAULT = "white"
COLOR_OBSTACLE = "black"
COLOR_START = "orange"
COLOR_END = "purple"
COLOR_OPEN = "lightgreen"
COLOR_CLOSED = "lightblue"
COLOR_PATH = "yellow"
COLOR_GRID = "grey"

# --- Screen Setup ---
screen = turtle.Screen()
screen.title("A* Pathfinding Algorithm Visualizer")
screen.setup(width=GRID_WIDTH * CELL_SIZE + 40, height=GRID_HEIGHT * CELL_SIZE + 40)
screen.bgcolor("black")
screen.tracer(0)

class Node:
    """Represents a single cell (node) in the grid."""
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.x = (col - GRID_WIDTH / 2 + 0.5) * CELL_SIZE
        self.y = (GRID_HEIGHT / 2 - row - 0.5) * CELL_SIZE
        self.color = COLOR_DEFAULT
        self.neighbors = []
        self.parent = None
        self.g_cost = float("inf")
        self.h_cost = float("inf")
        self.f_cost = float("inf")
    
    def __lt__(self, other):
        return self.f_cost < other.f_cost

def heuristic(node1, node2):
    return abs(node1.row - node2.row) + abs(node1.col - node2.col)

def reconstruct_path(current, draw_func):
    while current.parent:
        current = current.parent
        if current.color != COLOR_START:
            current.color = COLOR_PATH
        draw_func()

def a_star_algorithm(grid, start, end, draw_func):
    """The A* pathfinding algorithm."""
    count = 0
    open_set = [(0, start)]
    start.g_cost = 0
    start.f_cost = heuristic(start, end)

    while open_set:
        count += 1
        _, current = heapq.heappop(open_set)

        if current == end:
            reconstruct_path(current, draw_func)
            end.color = COLOR_END
            return True

        for neighbor in current.neighbors:
            temp_g_cost = current.g_cost + 1
            if temp_g_cost < neighbor.g_cost:
                neighbor.parent = current
                neighbor.g_cost = temp_g_cost
                neighbor.h_cost = heuristic(neighbor, end)
                neighbor.f_cost = neighbor.g_cost + neighbor.h_cost
                heapq.heappush(open_set, (neighbor.f_cost, neighbor))
        
        if count % SPEED_FACTOR == 0:
            draw_func()

        if current != start:
            current.color = COLOR_CLOSED
    
    return False

# --- Drawing Functions ---
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

def draw_node(node):
    pen.penup()
    pen.goto(node.x - CELL_SIZE / 2, node.y - CELL_SIZE / 2)
    pen.color(node.color)
    pen.begin_fill()
    for _ in range(4):
        pen.forward(CELL_SIZE)
        pen.left(90)
    pen.end_fill()

def draw_grid_lines():
    pen.color(COLOR_GRID)
    for i in range(GRID_HEIGHT + 1):
        y = (GRID_HEIGHT / 2 - i) * CELL_SIZE
        pen.penup()
        pen.goto(-GRID_WIDTH / 2 * CELL_SIZE, y)
        pen.pendown()
        pen.goto(GRID_WIDTH / 2 * CELL_SIZE, y)
    for i in range(GRID_WIDTH + 1):
        x = (i - GRID_WIDTH / 2) * CELL_SIZE
        pen.penup()
        pen.goto(x, GRID_HEIGHT / 2 * CELL_SIZE)
        pen.pendown()
        pen.goto(x, -GRID_HEIGHT / 2 * CELL_SIZE)

def draw_all(grid):
    pen.clear()
    for row in grid:
        for node in row:
            draw_node(node)
    draw_grid_lines()
    screen.update()

# --- User Interaction ---
def get_clicked_pos(x, y):
    col = int((x / CELL_SIZE) + GRID_WIDTH / 2)
    row = int((-y / CELL_SIZE) + GRID_HEIGHT / 2)
    if 0 <= row < GRID_HEIGHT and 0 <= col < GRID_WIDTH:
        return row, col
    return None

def main():
    # --- ADDED INSTRUCTIONS ---
    print("--- A* Pathfinding Visualizer ---")
    print("Controls:")
    print(" - Left Click: Place Start (1st), End (2nd), and Obstacles")
    print(" - Right Click: Erase a square")
    print(" - Spacebar: Run the algorithm")
    print(" - 'c': Clear the board")
    print("-----------------------------------")
    # --------------------------

    grid = [[Node(r, c) for c in range(GRID_WIDTH)] for r in range(GRID_HEIGHT)]
    start_node, end_node = None, None

    def on_click(x, y):
        nonlocal start_node, end_node
        pos = get_clicked_pos(x, y)
        if pos:
            node = grid[pos[0]][pos[1]]
            if not start_node:
                start_node = node
                node.color = COLOR_START
            elif not end_node and node != start_node:
                end_node = node
                node.color = COLOR_END
            elif node != start_node and node != end_node:
                node.color = COLOR_OBSTACLE
            draw_all(grid)

    def on_right_click(x, y):
        nonlocal start_node, end_node
        pos = get_clicked_pos(x, y)
        if pos:
            node = grid[pos[0]][pos[1]]
            if node == start_node: start_node = None
            if node == end_node: end_node = None
            node.color = COLOR_DEFAULT
            draw_all(grid)
            
    def start_algorithm():
        if start_node and end_node:
            for row in grid:
                for node in row:
                    if node.color != COLOR_OBSTACLE:
                        node.neighbors = []
                        if node.row > 0 and grid[node.row - 1][node.col].color != COLOR_OBSTACLE: node.neighbors.append(grid[node.row - 1][node.col])
                        if node.row < GRID_HEIGHT - 1 and grid[node.row + 1][node.col].color != COLOR_OBSTACLE: node.neighbors.append(grid[node.row + 1][node.col])
                        if node.col > 0 and grid[node.row][node.col - 1].color != COLOR_OBSTACLE: node.neighbors.append(grid[node.row][node.col - 1])
                        if node.col < GRID_WIDTH - 1 and grid[node.row][node.col + 1].color != COLOR_OBSTACLE: node.neighbors.append(grid[node.row][node.col + 1])
            
            a_star_algorithm(grid, start_node, end_node, lambda: draw_all(grid))
    
    def clear_board():
        nonlocal start_node, end_node
        start_node, end_node = None, None
        for row in grid:
            for node in row:
                node.color = COLOR_DEFAULT
                node.parent = None
                node.g_cost = float("inf")
                node.h_cost = float("inf")
                node.f_cost = float("inf")
        draw_all(grid)

    screen.listen()
    screen.onkey(start_algorithm, "space")
    screen.onkey(clear_board, "c")
    screen.onclick(on_click, 1)
    screen.onclick(on_right_click, 3)
    draw_all(grid)
    screen.mainloop()

main()