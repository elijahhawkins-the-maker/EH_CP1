#EH 1st random maze generator
import random as r
import turtle as t
t.screensize(500,500)
t.bgcolor("black")
t.begin_fill()
columns = [1,2,3,4,5,6,7,8,9,10,11,12]
rows = [1,2,3,4,5,6,7,8,9,10,11,12]
maze_size = 12
columns2 = 12
rows2 = 12
wall = 1
path = 0
maze = [[wall for i in range(maze_size)] for i in range(maze_size)]
linemaker = t.Turtle()
linemaker.speed(5000)
linemaker.shape("turtle")
linemaker.color("red")
linemaker.penup()
linemaker.goto(400,400)
linemaker.pendown()
linemaker.goto(66.6,400)
linemaker.penup()
linemaker.goto(0,400)
linemaker.pendown()
linemaker.goto(-400,400)
linemaker.goto(-400,-400)
linemaker.goto(-66.6,-400)
linemaker.penup()
linemaker.goto(0,-400)
linemaker.pendown()
linemaker.goto(400,-400)
linemaker.goto(400,400)
linemaker.left(90)
linemaker.left(90)
for y in range(maze_size):
    for x in range(maze_size):
        if maze[y][x] == wall:
            linemaker.left(90)
            linemaker.forward(66.6)
            linemaker.right(90)


def solvable(row_grid, col_grid):
    size = len(row_grid) - 1
    visited = set()
    stack = [(0,0)]

    while stack:
        x, y = stack.pop()

        if x == size - 1 and y == size - 1:
            return True
        if (x, y) in visited:
            continue
        visited.add((x, y))
        if x < size - 1 and col_grid[y][x+1] == 0:
            stack.append((x+1, y))
        if y < size - 1 and row_grid[y+1][x] == 0:
            stack.append((x, y+1))
        if x > 0 and col_grid[y][x] == 0:
            stack.append((x-1, y))
        if y > 0 and row_grid[y][x] == 0:
            stack.append((x, y-1))
    return False
def random():
    gen = t.Turtle()

random()

t.done()