import turtle as t
#import turtle at the top as t
#points for the very outside triangle
triangle_points = [(0,600), (-600,-300), (600,-300)]
#set parameters for the turtle and screen
gen = t.Turtle()
screen = t.Screen()
gen.hideturtle()
#set turtle speed to fastest
gen.speed(0)
#screen tracer at 0 makes it go even faster!
screen.tracer(0)

#draws the original triangle from its vertices
def triangle(point):
    gen.penup()
    gen.goto(point[0])
    gen.pendown()
    gen.goto(point[1])
    gen.goto(point[2])
    gen.goto(point[0])

#calculates the midpoint of a side of the triangle through the two vertices on both sides
def midpoint(p1,p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

#here is where the actual recursion happens!
#function for fractal generation
def sierpinski(point, depth):
    #generates triangle using point parameters set in main.py
    triangle(point)
    #if statement that checks whether to keep generating triangles or not
    if depth > 0:
        #has a list of the vertices of each individual triangle, based on the depth entered in main.py, then removes 1 from the depth once it is done
        sierpinski([point[0], midpoint(point[0], point[1]), midpoint(point[0], point[2])], depth - 1)
        sierpinski([point[1], midpoint(point[0], point[1]), midpoint(point[1], point[2])], depth - 1)
        sierpinski([point[2], midpoint(point[2], point[1]), midpoint(point[0], point[2])], depth - 1)

#this runs it separately so that the choices in main.py work
def run(depth, back, color):
    #makes it so that colors can be entered as a string
    t.colormode(1.0)
    #changes the color to the user input
    t.bgcolor(back)
    gen.color(color)
    #clears anything that was originally on it
    gen.clear()
    #executes the code for sierpinski generation
    sierpinski(triangle_points, depth)
    #updates the turtle screen once the code is done
    screen.update() 