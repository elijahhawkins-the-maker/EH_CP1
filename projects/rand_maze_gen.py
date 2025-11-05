#EH 1st random maze generator
import random as r
import turtle as t
t.screensize(500,500)
t.bgcolor("black")


linemaker = t.Turtle()
t.begin_fill()
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
for i in range(1,7):
    linemaker.forward(66.6)
    linemaker.left(90)
    linemaker.forward(800)
    linemaker.right(90)
    linemaker.forward(66.6)
    linemaker.right(90)
    linemaker.forward(800)
    linemaker.left(90)
    if linemaker.xcor() > -400 and linemaker.xcor() < -399:
        for i in range(1,6):
            linemaker.left(90)
            linemaker.forward(66.6)
            linemaker.left(90)
            linemaker.forward(800)
            linemaker.right(90)
            linemaker.forward(66.6)
            linemaker.right(90)
            linemaker.forward(800)
        linemaker.left(90)
        linemaker.forward(66.6)
        linemaker.left(90)
        linemaker.forward(800)

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
columns = []
def random():
    gen = t.Turtle()
    gen.pensize(5)
    gen.color("black")
    gen.speed(5000)
    gen.goto(-66.6,400)
    for i in range(1,10000):
        gen.forward(r.randint(1, 66))
        gen.left(90)
        gen.forward(r.randint(1,66))
        gen.right(90)
        gen.forward(r.randint(1,66))
        if gen.ycor() >= 350 or gen.ycor() <= -350:
            gen.penup()
            gen.goto(r.randint(0,250),r.randint(0,250))
            gen.pendown()
        if gen.xcor() >= 350 or gen.xcor() <= -350:
            gen.penup()
            gen.goto(r.randint(0,250),r.randint(0,250))
            gen.pendown()
random()

t.done()