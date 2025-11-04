import turtle
import random
import time

# --- Maze Configuration ---
MAZE_SIZE = 21 # Must be an odd number to work correctly with the algorithm
CELL_SIZE = 20 # Size of each cell in pixels
WALL = 1
PATH = 0
# ---------------------------

# Set up the Turtle screen
screen = turtle.Screen()
screen.setup(MAZE_SIZE * CELL_SIZE + 50, MAZE_SIZE * CELL_SIZE + 50)
screen.title("Random Maze Generator (Two Openings)")
screen.tracer(0) # Turn off automatic screen updates for faster drawing

# Maze data structure (initially all walls)
maze = [[WALL for _ in range(MAZE_SIZE)] for _ in range(MAZE_SIZE)]

# Turtle for drawing the maze
maze_turtle = turtle.Turtle()
maze_turtle.speed(0)
maze_turtle.hideturtle()
maze_turtle.penup()

def draw_maze():
    """Draws the maze based on the maze data structure."""
    maze_turtle.clear()
    for y in range(MAZE_SIZE):
        for x in range(MAZE_SIZE):
            if maze[y][x] == WALL:
                draw_wall(x, y)
    screen.update()

def draw_wall(x, y):
    """Draws a single wall block at grid coordinates (x, y)."""
    # Convert grid coordinates to screen coordinates
    screen_x = (x - MAZE_SIZE // 2) * CELL_SIZE
    screen_y = (MAZE_SIZE // 2 - y) * CELL_SIZE
    
    maze_turtle.goto(screen_x, screen_y)
    maze_turtle.pendown()
    maze_turtle.begin_fill()
    for _ in range(4):
        maze_turtle.forward(CELL_SIZE)
        maze_turtle.right(90)
    maze_turtle.end_fill()
    maze_turtle.penup()

def generate_maze(x, y):
    """Recursive backtracker algorithm to generate the maze."""
    maze[y][x] = PATH
    
    # Get a list of unvisited neighbors
    neighbors = []
    if x > 1 and maze[y][x - 2] == WALL: neighbors.append((x - 2, y)) # Left
    if x < MAZE_SIZE - 2 and maze[y][x + 2] == WALL: neighbors.append((x + 2, y)) # Right
    if y > 1 and maze[y - 2][x] == WALL: neighbors.append((x, y - 2)) # Up
    if y < MAZE_SIZE - 2 and maze[y + 2][x] == WALL: neighbors.append((x, y + 2)) # Down
    
    random.shuffle(neighbors)
    
    for nx, ny in neighbors:
        if maze[ny][nx] == WALL:
            # Carve path (remove wall between current cell and neighbor)
            wall_x, wall_y = (x + nx) // 2, (y + ny) // 2
            maze[wall_y][wall_x] = PATH
            generate_maze(nx, ny)

# --- Main execution ---

# 1. Generate the maze using the recursive function
# Start generation from a random odd cell within the grid
start_x, start_y = (random.randrange(1, MAZE_SIZE, 2), random.randrange(1, MAZE_SIZE, 2))
generate_maze(start_x, start_y)

# 2. Create the two openings (start and end)

# Define an entrance at the top center
entrance_x = MAZE_SIZE // 2
entrance_y = 0
maze[entrance_y][entrance_x] = PATH 
# Carve a path into the first row
maze[entrance_y + 1][entrance_x] = PATH

# Define an exit at the bottom center
exit_x = MAZE_SIZE // 2
exit_y = MAZE_SIZE - 1
maze[exit_y][exit_x] = PATH
# Carve a path into the last row
maze[exit_y - 1][exit_x] = PATH


# 3. Draw the final maze
draw_maze()

turtle.done()