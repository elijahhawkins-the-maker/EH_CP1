#EH 1st random maze generator
#import random as r and turtle as t at the top of the code
import random as r
import turtle as t
#this makes the screen size 500 pixels by 500 pixels
t.screensize(500,500)
#this makes the background color black
t.bgcolor("black")
#this starts the filling of color for the turtle
t.begin_fill()
#these two functions make the maze draw instantly
screen = t.Screen()
screen.tracer(0)
#these variables set what the walls and paths are numerically
wall = 1
path = 0
#this defines the linemaker
linemaker = t.Turtle()
#sets the speed to 10
linemaker.speed(10)
#makes it look like a turtle
linemaker.shape("turtle")
#makes the color of the turtle red
linemaker.color("red")
#this is the function that defines the outer walls of the maze
def walls():
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
    linemaker.penup()
    linemaker.goto(-400,-333.4)
    linemaker.pendown()
walls()
#this allows for each of the cells to be a random number between 0 and 1 to generate either a wall or a path (could have been done easier but I didn't know how)
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

#this is the function for the random generation
def random():
    bruh = 0
    #this sets the variable to 0 before the while loop
    while True:
            #this breaks the while loop once the turtle crosses the maze
            if bruh == 12:
                break
            #these 2 if statements check whether the random int is a 0 or 1 and makes it draw or not
            if gridrow[0][bruh] == wall:
                linemaker.pendown()
                linemaker.forward(66.6)
            if gridrow[0][bruh] == path:
                linemaker.penup()
                linemaker.forward(66.6)
            #this adds one after each time it moves forward a unit (66.6 pixels)
            bruh += 1
    #this turns the turtle the other way, then moves it up one unit to draw the next row
    linemaker.left(90)
    linemaker.forward(66.6)
    linemaker.left(90)
    #every single line after these are basically carbon copies of eachother, but they have 1 higher position in the list, and they turn right, then left, each time
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
    #Now the turtle has to turn all the way around to begin drawing the columns
    linemaker.left(90)
    linemaker.forward(66.6)
    linemaker.left(90)
    linemaker.forward(66.6)
    linemaker.left(90)
    linemaker.penup()
    linemaker.goto(-400,400)
    linemaker.pendown()
    #these while loops are also all carbon copies, but they use the random columns instead of the rows
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
    linemaker.right(90)
    linemaker.forward(66.6)
    linemaker.right(90)
#this is the function that was given in class to see if it was solvable
random()
def solvable(row_grid, col_grid):
    size = len(row_grid)
    visited = set()
    stack = [(0,0)]

    while stack:
        x, y = stack.pop()

        if x == size - 1 and y == size - 1:
            return True
        if (x, y) in visited:
            continue
        visited.add((x, y))
        if x + 1 < size and col_grid[y][x+1] == 0:
            stack.append((x+1, y))
        if y + 1 < size and row_grid[y+1][x] == 0:
            stack.append((x, y+1))
        if x > 0 and col_grid[y][x] == 0:
            stack.append((x-1, y))
        if y > 0 and row_grid[y][x] == 0:
            stack.append((x, y-1))
    return False
#this checks the lists to see if the maze can be solved
is_solvable = solvable(gridrow, gridcol)
#if statements that check if the function is true
if is_solvable:
    print("the maze is solvable")
else:
    print("the maze isn't solvable")
#keeps the window open
t.done()