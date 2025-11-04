#EH 1st random maze generator
import random as r
import turtle as t
t.screensize(500,500)
t.bgcolor("black")

WIDTH = 8  # Must be odd for walls to work well
HEIGHT = 8 # Must be odd
CELL_SIZE = 7
maze = [[1 for _ in range(WIDTH)] for _ in range(HEIGHT)]
linemaker = t.Turtle()
t.begin_fill()
linemaker.speed(5000)
linemaker.shape("turtle")
linemaker.color("red")
linemaker.penup()
linemaker.goto(400,400)
linemaker.pendown()
linemaker.goto(10,400)
linemaker.penup()
linemaker.goto(-10,400)
linemaker.pendown()
linemaker.goto(-400,400)
linemaker.goto(-400,-400)
linemaker.goto(-10,-400)
linemaker.penup()
linemaker.goto(10,-400)
linemaker.pendown()
linemaker.goto(400,-400)
linemaker.goto(400,400)
linemaker.left(90)
linemaker.left(90)
for i in range(1,8):
    linemaker.forward(60)
    linemaker.left(90)
    linemaker.forward(400)
    break
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
t.done()