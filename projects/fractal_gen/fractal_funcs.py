import turtle as t

triangle_points = [(0,600), (-600,-300), (600,-300)]

gen = t.Turtle()
screen = t.Screen()
gen.hideturtle()
gen.speed(0)
screen.tracer(0)

def triangle(point):
    gen.penup()
    gen.goto(point[0])
    gen.pendown()
    gen.goto(point[1])
    gen.goto(point[2])
    gen.goto(point[0])

def midpoint(p1,p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(point, depth):

    triangle(point)

    if depth > 0:
        sierpinski([point[0], midpoint(point[0], point[1]), midpoint(point[0], point[2])], depth - 1)
        sierpinski([point[1], midpoint(point[0], point[1]), midpoint(point[1], point[2])], depth - 1)
        sierpinski([point[2], midpoint(point[2], point[1]), midpoint(point[0], point[2])], depth - 1)

def run(depth, back, color):
    t.colormode(1.0)
    t.bgcolor(back)
    gen.color(color)
    gen.clear()
    
    sierpinski(triangle_points, depth)
    
    screen.update() 