import turtle as t

def choices():
    screen.tracer(0)
    color = t.textinput("Turtle Color", "What is the color that you would like the triangle to be?\n").lower()
    if color:
        t.color(color)
    background = t.textinput("Background Color", "Now what is the background color that you would like it to be?\n").lower()
    if background:
        t.Screen().bgcolor(background)
    sierpinski(triangle_points, 8)

gen = t.Turtle()
screen = t.Screen()

gen.shape("blank")
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

t.begin_fill()
def sierpinski(point, depth):
    triangle(point)

    if depth > 0:
        sierpinski([point[0], midpoint(point[0], point[1]), midpoint(point[0], point[2])], depth - 1)
        sierpinski([point[1], midpoint(point[0], point[1]), midpoint(point[1], point[2])], depth - 1)
        sierpinski([point[2], midpoint(point[2], point[1]), midpoint(point[0], point[2])], depth - 1)
    screen.update()
    screen.ontimer(sierpinski, 0)

triangle_points = [(0,600), (-600,-300), (600,-300)]
t.end_fill()

t.done()