import turtle as t

gen = t.Turtle()
screen = t.Screen()

gen.fillcolor("purple")
gen.shape("turtle")

point_1 = (0,200)
point_2 = (-200, -100)
point_3 = (200, -100)


def triangle():
    gen.penup()
    gen.goto(point_1)
    gen.pendown()
    gen.goto(point_2)
    gen.goto(point_3)
    gen.goto(point_1)
triangle()
t.done()

def midpoint(p1,p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

mid_1 = midpoint(point_1, point_2)
mid_2 = midpoint(point_2, point_3)
mid_3 = midpoint(point_1, point_3)

def sierpinski():
    for x in range(6):
        gen.goto(mid_1)
        gen.goto(mid_2)
        gen.goto(mid_3)
        gen.goto(midpoint(mid_1,mid_2))
        gen.goto(midpoint(mid_2,mid_3))
        gen.goto(midpoint(mid_1,mid_3))
sierpinski()