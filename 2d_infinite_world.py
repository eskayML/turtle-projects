import turtle
import math

from collections.abc import Generator
from enum import IntEnum

TILE_RATIO = 0.025          # Ratio of tile size to screen width
CLEAR_COLOR = (0, 125, 255) # Color to clear screen (blue)
UPDATE_FREQUENCY_MS = 16    # How often to call the update function in ms
CHUNK_LENGTH = 64           # World split into chunks, length of one chunk in tiles
GENERATE_WAVELENGTH = 8     # How often a new random point is generated in noise function (every multiple of x)
GENERATE_OCTAVES = 4        # Number of layers of noise we overlay
GENERATE_AMPLITUDE = 8      # Multiplier of noise, determines steepness of terrian
WORLD_SEED = 0              # Seed of noise (same seed -> same world)
TREE_OFFSET = 158573        # Offset noise so tree generation chance at some tile doesn't correspond to world height at that tile

class Tile(IntEnum):
    AIR = 0,
    GRASS = 1,
    DIRT = 2,
    STONE = 3,
    LOG = 4,
    LEAVES = 5

# Offset by 1, since air isn't rendered
TILE_COLORS = [
    (  0, 200,   0), # Grass
    (150, 100,  50), # Dirt
    (100, 100, 100), # Stone
    (200, 150, 100), # Log
    (  0, 255,  50)  # Leaves
]

# Helper functions
def vec2_add(a : tuple, b : tuple):
    return (a[0] + b[0], a[1] + b[1])

def vec2_sub(a : tuple, b : tuple):
    return (a[0] - b[0], a[1] - b[1])

def vec2_mul(v : tuple, s : float):
    return (v[0] * s, v[1] * s)

class World:
    def __init__(self):
        # Stores chunks (lists of tiles)
        self.chunks = []
        # Stores position of that chunk in world
        self.chunk_indices = []

    def update(self, player_position : tuple[int, int]):
        # Calculate chunk player is in
        player_chunk_position = (math.floor(player_position[0] / CHUNK_LENGTH), math.floor(player_position[1] / CHUNK_LENGTH))

        new_chunks = []
        new_chunk_indices = []

        # Generate all chunks in square radius 1 of player
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                required_chunk = vec2_sub(player_chunk_position, (dx, dy))

                for i, chunk in enumerate(self.chunk_indices):
                    if chunk == required_chunk:
                        new_chunks.append(self.chunks[i])
                        new_chunk_indices.append(chunk)

                        break
                else:
                    new_chunks.append(generate_chunk(required_chunk))
                    new_chunk_indices.append(required_chunk)

        self.chunks = new_chunks
        self.chunk_indices = new_chunk_indices

# State
tile_size = None
window_width = None
window_height = None

world = World()
player_position = (0, 0)
camera_position = None
player_direction = (0, 0)

def generate_tree(tiles : list[Tile], base_position : tuple[int, int]):
    """
    Generate a tree at a given position (base position is where the stump of the tree)
    """
    TREE_LOG_HEIGHT = 3
    TREE_LEAVES_HEIGHT = 3
    TREE_LEAVES_WIDTH = 5
    TREE_LEAVES_HALFWIDTH = math.ceil((TREE_LEAVES_WIDTH - 1) / 2)
    TREE_TOTAL_HEIGHT = TREE_LOG_HEIGHT + TREE_LEAVES_HEIGHT

    # Check x within bounds
    if base_position[0] >= TREE_LEAVES_HALFWIDTH - 1 and base_position[0] < CHUNK_LENGTH - TREE_LEAVES_HALFWIDTH:
        if base_position[1] <= CHUNK_LENGTH - TREE_TOTAL_HEIGHT:
            # Build log
            for y_off in range(TREE_LOG_HEIGHT):
                y = base_position[1] + y_off

                tiles[y * CHUNK_LENGTH + base_position[0]] = Tile.LOG

            # Build leaves layers
            for y_off in range(TREE_LEAVES_HEIGHT):
                y = base_position[1] + y_off + TREE_LOG_HEIGHT

                # NOTE: Extra math to make leaves taper off at top level
                for x_off in range(-TREE_LEAVES_HALFWIDTH + (y_off == TREE_LEAVES_HEIGHT - 1), TREE_LEAVES_HALFWIDTH + 1 - (y_off == TREE_LEAVES_HEIGHT - 1)):
                    x = base_position[0] + x_off

                    tiles[y * CHUNK_LENGTH + x] = Tile.LEAVES


def generate_chunk(chunk_index : tuple[int, int]):
    """
    Generate a chunk's tiles at a given index, returning a 1D array of tiles
    """
    # Calculate tile position of bottom left of chunk
    position = vec2_mul(chunk_index, CHUNK_LENGTH)

    tiles = [Tile.AIR] * (CHUNK_LENGTH * CHUNK_LENGTH)

    # For each x slice
    for x in range(CHUNK_LENGTH):
        # Get a noise value, and calculate height we should generate up to
        sampled_noise = noise(position[0] + x, GENERATE_WAVELENGTH, GENERATE_OCTAVES) * GENERATE_AMPLITUDE
        height = math.floor(sampled_noise) - position[1]

        for y in range(CHUNK_LENGTH):
            index = x + y * CHUNK_LENGTH
            selected_tile = None

            # If we're above maximum height, stop generating any higher
            if y > height:
                break
            # If we're at maximum height, generate grass
            elif y == height:
                selected_tile = Tile.GRASS
            # Generate topsoil
            elif height - y <= 3:
                selected_tile = Tile.DIRT
            # Generate stone below maximum height
            else:
                selected_tile = Tile.STONE

            # Set the tile in tiles array
            tiles[index] = selected_tile

        # Add trees randomly
        if noise(position[0] + x + TREE_OFFSET, 1, 1) < 0.1:
            generate_tree(tiles, (x, height + 1))
            
    return tiles

def interp(a : float, b : float, t : float) -> float:
    """
    Linearly interpolate between two points given a speed (t)
    """
    return a * (1 - t) + b * t

def int_hash(x : int) -> float:
    """
    Hash integer to float
    """
    x = x ^ WORLD_SEED
    # https://stackoverflow.com/questions/664014/what-integer-hash-function-are-good-that-accepts-an-integer-hash-key
    x = ((x >> 16) ^ x) * 0x45d9f3b
    x = ((x >> 16) ^ x) * 0x45d9f3b
    x = ((x >> 16) ^ x)
    
    return x % (2 ** 32) / (2 ** 32)

def noise(x : int, wavelength : int, octaves : int) -> Generator[float, None, None]:
    """
    Generate linearly interpolated white noise at some x value
    """
    # Generate two lattice points
    lattice_0 = int_hash(x // wavelength)
    lattice_1 = int_hash(x // wavelength + 1)

    noise_sum = 0
    amplitude_sum = 0
    amplitude = 1

    for _ in range(octaves):
        amplitude_sum += amplitude
        # Linearly interpolate between lattice points, biases towards whichever side we're closer to
        noise_sum += interp(lattice_0, lattice_1, (x % wavelength) / wavelength) * amplitude
        
        amplitude *= 0.5
        wavelength *= 0.5

    return noise_sum / amplitude_sum

def draw_tile(x : float, y : float, tile : Tile) -> None:
    """
    Use turtle to draw tile at some position
    """
    if tile == Tile.AIR: return

    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor(TILE_COLORS[tile - 1])
    turtle.pendown()

    turtle.begin_fill()

    # Square
    for _ in range(4):
        turtle.forward(tile_size)
        turtle.left(90)

    turtle.end_fill()

def aabb_check(min1 : tuple[float, float], max1 : tuple[float, float], min2 : tuple[float, float], max2 : tuple[float, float]):
    """
    Check if two AABBs are intersecting
    """
    return not (max1[0] <= min2[0] or max2[0] <= min1[0]) and (max1[1] <= min2[1] or max2[1] <= min1[1])

def update():
    """
    Update screen, game, player
    """
    global tile_size, window_width, window_height, camera_position, player_position, player_direction

    # Clear screen
    turtle.clear()

    # Get window dimensions
    window_width = float(turtle.window_width())
    window_height = float(turtle.window_height())
    half_window = vec2_mul((window_width, window_height), 0.5)

    # Calculate tile size
    tile_size = window_width * TILE_RATIO

    # Player movement
    player_position = vec2_add(player_position, player_direction)
    player_direction = (0, 0)

    # Update camera position
    camera_position = vec2_add(vec2_mul(player_position, tile_size), half_window)

    # Update world around player
    world.update(player_position)

    # For each loaded chunk
    for i, chunk_index in enumerate(world.chunk_indices):
        chunk = world.chunks[i]

        for y in range(CHUNK_LENGTH):
            draw_y = (y + chunk_index[1] * CHUNK_LENGTH) * tile_size - camera_position[1]

            # Bounds check y draw coordinate
            if not (draw_y >= -half_window[1] and draw_y <= half_window[1]):
                continue

            for x in range(CHUNK_LENGTH):
                tile = chunk[y * CHUNK_LENGTH + x]

                draw_x = (x + chunk_index[0] * CHUNK_LENGTH) * tile_size - camera_position[0]

                # Bounds check x draw coordinate
                if draw_x >= -half_window[0] and draw_x <= half_window[0]:
                    draw_tile(draw_x, draw_y, tile)

    turtle.update()
    turtle.ontimer(update, t=UPDATE_FREQUENCY_MS)

def add_direction(direction : tuple[int, int]):
    """
    Update moving direction of player
    """
    global player_direction
    player_direction = vec2_add(player_direction, direction)
    screen.update()

if __name__ == "__main__":
    # Make turtle fast
    turtle.speed(0)
    turtle.tracer(False)
    # Hide turtle sprite
    turtle.hideturtle()
    turtle.colormode(0xff)
    turtle.pencolor(CLEAR_COLOR)
    turtle.bgcolor(CLEAR_COLOR)

    print("Use WASD to navigate")

    screen = turtle.Screen()
    screen.onkeypress(lambda: add_direction((-1,  0)), "a")
    screen.onkeypress(lambda: add_direction(( 1,  0)), "d")
    screen.onkeypress(lambda: add_direction(( 0,  1)), "w")
    screen.onkeypress(lambda: add_direction(( 0, -1)), "s")

    turtle.listen()

    update()

    turtle.mainloop()