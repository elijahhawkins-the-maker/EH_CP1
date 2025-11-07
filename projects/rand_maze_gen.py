#EH 1st random maze generator
import random as r
import turtle as t
import time as ti
t.screensize(500,500)
t.bgcolor("black")
t.begin_fill()
screen = t.Screen()
columns = [1,2,3,4,5,6,7,8,9,10,11,12]
rows = [1,2,3,4,5,6,7,8,9,10,11,12]
maze_size = 12
columns2 = 12
rows2 = 12
wall = 1
path = 0
maze = [[wall for i in range(maze_size)] for i in range(maze_size)]
linemaker = t.Turtle()
linemaker.speed(10)
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
linemaker.teleport(-400,-333.4)

gridrow = [
        [r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)],
        [r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)],
        [r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)],
        [r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)],
        [r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)],
        [r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)],
        [r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)],
        [r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)],
        [r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)],
        [r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)],
        [r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)]]

gridcol = [
        [r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)],
        [r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)],
        [r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)],
        [r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)],
        [r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)],
        [r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)],
        [r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)],
        [r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)],
        [r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)],
        [r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)],
        [r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)]]

bruh = 0
while True:
        if bruh == 12:
            break
        if gridrow[0][bruh] == wall:
            linemaker.pendown()
            linemaker.forward(66.6)
        if gridrow[0][bruh] == path:
            linemaker.penup()
            linemaker.forward(66.6)
        bruh += 1
linemaker.left(90)
linemaker.forward(66.6)
linemaker.left(90)
bruh = 0
while True:
        if bruh == 12:
            break
        if gridrow[1][bruh] == wall:
            linemaker.pendown()
            linemaker.forward(66.6)
        if gridrow[1][bruh] == path:
            linemaker.penup()
            linemaker.forward(66.6)
        bruh += 1
linemaker.right(90)
linemaker.forward(66.6)
linemaker.right(90)
bruh = 0
while True:
        if bruh == 12:
            break
        if gridrow[2][bruh] == wall:
            linemaker.pendown()
            linemaker.forward(66.6)
        if gridrow[2][bruh] == path:
            linemaker.penup()
            linemaker.forward(66.6)
        bruh += 1
linemaker.left(90)
linemaker.forward(66.6)
linemaker.left(90)
bruh = 0
while True:
        if bruh == 12:
            break
        if gridrow[3][bruh] == wall:
            linemaker.pendown()
            linemaker.forward(66.6)
        if gridrow[3][bruh] == path:
            linemaker.penup()
            linemaker.forward(66.6)
        bruh += 1
linemaker.right(90)
linemaker.forward(66.6)
linemaker.right(90)
bruh = 0
while True:
        if bruh == 12:
            break
        if gridrow[4][bruh] == wall:
            linemaker.pendown()
            linemaker.forward(66.6)
        if gridrow[4][bruh] == path:
            linemaker.penup()
            linemaker.forward(66.6)
        bruh += 1
linemaker.left(90)
linemaker.forward(66.6)
linemaker.left(90)
bruh = 0
while True:
        if bruh == 12:
            break
        if gridrow[5][bruh] == wall:
            linemaker.pendown()
            linemaker.forward(66.6)
        if gridrow[5][bruh] == path:
            linemaker.penup()
            linemaker.forward(66.6)
        bruh += 1
linemaker.right(90)
linemaker.forward(66.6)
linemaker.right(90)
bruh = 0
while True:
        if bruh == 12:
            break
        if gridrow[6][bruh] == wall:
            linemaker.pendown()
            linemaker.forward(66.6)
        if gridrow[6][bruh] == path:
            linemaker.penup()
            linemaker.forward(66.6)
        bruh += 1
linemaker.left(90)
linemaker.forward(66.6)
linemaker.left(90)
bruh = 0
while True:
        if bruh == 12:
            break
        if gridrow[7][bruh] == wall:
            linemaker.pendown()
            linemaker.forward(66.6)
        if gridrow[7][bruh] == path:
            linemaker.penup()
            linemaker.forward(66.6)
        bruh += 1
linemaker.right(90)
linemaker.forward(66.6)
linemaker.right(90)
bruh = 0
while True:
        if bruh == 12:
            break
        if gridrow[8][bruh] == wall:
            linemaker.pendown()
            linemaker.forward(66.6)
        if gridrow[8][bruh] == path:
            linemaker.penup()
            linemaker.forward(66.6)
        bruh += 1
linemaker.left(90)
linemaker.forward(66.6)
linemaker.left(90)
bruh = 0
while True:
        if bruh == 12:
            break
        if gridrow[9][bruh] == wall:
            linemaker.pendown()
            linemaker.forward(66.6)
        if gridrow[9][bruh] == path:
            linemaker.penup()
            linemaker.forward(66.6)
        bruh += 1
linemaker.right(90)
linemaker.forward(66.6)
linemaker.right(90)
bruh = 0
while True:
        if bruh == 12:
            break
        if gridrow[10][bruh] == wall:
            linemaker.pendown()
            linemaker.forward(66.6)
        if gridrow[10][bruh] == path:
            linemaker.penup()
            linemaker.forward(66.6)
        bruh += 1
linemaker.left(90)
linemaker.forward(66.6)
linemaker.left(90)
linemaker.forward(66.6)
linemaker.left(90)
linemaker.teleport(-400,400)
bruh = 0
while True:
        if bruh == 12:
            break
        if gridcol[0][bruh] == wall:
            linemaker.pendown()
            linemaker.forward(66.6)
        if gridcol[0][bruh] == path:
            linemaker.penup()
            linemaker.forward(66.6)
        bruh += 1
linemaker.left(90)
linemaker.forward(66.6)
linemaker.left(90)
bruh = 0
while True:
        if bruh == 12:
            break
        if gridcol[1][bruh] == wall:
            linemaker.pendown()
            linemaker.forward(66.6)
        if gridcol[1][bruh] == path:
            linemaker.penup()
            linemaker.forward(66.6)
        bruh += 1
linemaker.right(90)
linemaker.forward(66.6)
linemaker.right(90)
bruh = 0
while True:
        if bruh == 12:
            break
        if gridcol[2][bruh] == wall:
            linemaker.pendown()
            linemaker.forward(66.6)
        if gridcol[2][bruh] == path:
            linemaker.penup()
            linemaker.forward(66.6)
        bruh += 1
linemaker.left(90)
linemaker.forward(66.6)
linemaker.left(90)
bruh = 0
while True:
        if bruh == 12:
            break
        if gridcol[3][bruh] == wall:
            linemaker.pendown()
            linemaker.forward(66.6)
        if gridcol[3][bruh] == path:
            linemaker.penup()
            linemaker.forward(66.6)
        bruh += 1
linemaker.right(90)
linemaker.forward(66.6)
linemaker.right(90)
bruh = 0
while True:
        if bruh == 12:
            break
        if gridcol[4][bruh] == wall:
            linemaker.pendown()
            linemaker.forward(66.6)
        if gridcol[4][bruh] == path:
            linemaker.penup()
            linemaker.forward(66.6)
        bruh += 1
linemaker.left(90)
linemaker.forward(66.6)
linemaker.left(90)
bruh = 0
while True:
        if bruh == 12:
            break
        if gridcol[5][bruh] == wall:
            linemaker.pendown()
            linemaker.forward(66.6)
        if gridcol[5][bruh] == path:
            linemaker.penup()
            linemaker.forward(66.6)
        bruh += 1
linemaker.right(90)
linemaker.forward(66.6)
linemaker.right(90)
bruh = 0
while True:
        if bruh == 12:
            break
        if gridcol[6][bruh] == wall:
            linemaker.pendown()
            linemaker.forward(66.6)
        if gridcol[6][bruh] == path:
            linemaker.penup()
            linemaker.forward(66.6)
        bruh += 1
linemaker.left(90)
linemaker.forward(66.6)
linemaker.left(90)
bruh = 0
while True:
        if bruh == 12:
            break
        if gridcol[7][bruh] == wall:
            linemaker.pendown()
            linemaker.forward(66.6)
        if gridcol[7][bruh] == path:
            linemaker.penup()
            linemaker.forward(66.6)
        bruh += 1
linemaker.right(90)
linemaker.forward(66.6)
linemaker.right(90)
bruh = 0
while True:
        if bruh == 12:
            break
        if gridcol[8][bruh] == wall:
            linemaker.pendown()
            linemaker.forward(66.6)
        if gridcol[8][bruh] == path:
            linemaker.penup()
            linemaker.forward(66.6)
        bruh += 1
linemaker.left(90)
linemaker.forward(66.6)
linemaker.left(90)
bruh = 0
while True:
        if bruh == 12:
            break
        if gridcol[9][bruh] == wall:
            linemaker.pendown()
            linemaker.forward(66.6)
        if gridcol[9][bruh] == path:
            linemaker.penup()
            linemaker.forward(66.6)
        bruh += 1
linemaker.right(90)
linemaker.forward(66.6)
linemaker.right(90)
bruh = 0
while True:
        if bruh == 12:
            break
        if gridcol[10][bruh] == wall:
            linemaker.pendown()
            linemaker.forward(66.6)
        if gridcol[10][bruh] == path:
            linemaker.penup()
            linemaker.forward(66.6)
        bruh += 1
linemaker.left(90)
linemaker.forward(66.6)
linemaker.left(90)
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