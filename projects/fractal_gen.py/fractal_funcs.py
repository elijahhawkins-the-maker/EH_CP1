import turtle as t

gen = t.Turtle()
screen = t.Screen()

t.bgcolor("black")

gen.color("green")
gen.shape("turtle")
gen.speed(0)

screen.tracer(0)

point_1 = (0,200)
point_2 = (-200, -100)
point_3 = (200, -100)

def triangle(point):
    gen.penup()
    gen.goto(point[0])
    gen.pendown()
    gen.goto(point[1])
    gen.goto(point[2])
    gen.goto(point[0])


def midpoint(p1,p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

mid_1 = midpoint(point_1, point_2)
mid_2 = midpoint(point_2, point_3)
mid_3 = midpoint(point_1, point_3)

def sierpinski(point, depth):
    triangle(point)

    if depth > 0:
        sierpinski([point[0], midpoint(point[0], point[1]), midpoint(point[0], point[2])], depth - 1)
        sierpinski([point[1], midpoint(point[0], point[1]), midpoint(point[1], point[2])], depth - 1)
        sierpinski([point[2], midpoint(point[2], point[1]), midpoint(point[0], point[2])], depth - 1)
    screen.update()
    screen.ontimer(sierpinski, 20)

triangle_points = [(0,200), (-200,-100), (200,-100)]

sierpinski(triangle_points, 7)
gen.hideturtle()
t.done()