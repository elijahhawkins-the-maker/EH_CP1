#EH 1st random maze generator
import random
import turtle as t
t.screensize(500,500)
t.bgcolor("black")

massive = []

line_maker = t.Turtle()
t.begin_fill()
line_maker.speed(5000)
line_maker.shape("turtle")
line_maker.color("red")
line_maker.penup()
line_maker.goto(400,400)
line_maker.pendown()
line_maker.goto(10,400)
line_maker.penup()
line_maker.goto(-10,400)
line_maker.pendown()
line_maker.goto(-400,400)
line_maker.goto(-400,-400)
line_maker.goto(-10,-400)
line_maker.penup()
line_maker.goto(10,-400)
line_maker.pendown()
line_maker.goto(400,-400)
line_maker.goto(400,400)

for x in range(1,20):
    line_maker.penup()
    line_maker.goto(400,400)
t.done()

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