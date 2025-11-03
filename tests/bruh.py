import turtle
import random

# Maze dimensions and cell size
WIDTH = 21  # Must be odd for walls to work well
HEIGHT = 21 # Must be odd
CELL_SIZE = 20

# Initialize maze grid with walls
maze = [[1 for _ in range(WIDTH)] for _ in range(HEIGHT)] # 1 for wall, 0 for path

# Turtle setup
screen = turtle.Screen()
screen.setup(WIDTH * CELL_SIZE + 50, HEIGHT * CELL_SIZE + 50)
screen.tracer(0) # Turn off screen updates for faster drawing
t = turtle.Turtle()
t.speed('fastest')
t.penup()
t.hideturtle()

def draw_maze():
    t.clear()
    t.goto(-WIDTH * CELL_SIZE / 2, HEIGHT * CELL_SIZE / 2) # Start top-left
    for r in range(HEIGHT):
        for c in range(WIDTH):
            if maze[r][c] == 1: # If it's a wall
                t.pendown()
                t.begin_fill()
                for _ in range(4):
                    t.forward(CELL_SIZE)
                    t.right(90)
                t.end_fill()
                t.penup()
            t.forward(CELL_SIZE)
        t.goto(-WIDTH * CELL_SIZE / 2, HEIGHT * CELL_SIZE / 2 - (r + 1) * CELL_SIZE)
    screen.update()

def generate_maze(x, y):
    maze[y][x] = 0 # Mark current cell as path

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] # E, W, S, N
    random.shuffle(directions)

    for dx, dy in directions:
        nx, ny = x + 2 * dx, y + 2 * dy # Neighbor cell (skipping a wall)
        wall_x, wall_y = x + dx, y + dy # Wall between current and neighbor

        if 0 <= nx < WIDTH and 0 <= ny < HEIGHT and maze[ny][nx] == 1:
            maze[wall_y][wall_x] = 0 # Carve out path through wall
            generate_maze(nx, ny)

# Start maze generation from an odd-indexed cell (to ensure a path)
generate_maze(0, 0)
draw_maze()
turtle.done()