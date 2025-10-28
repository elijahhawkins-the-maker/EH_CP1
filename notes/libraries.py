#EH 1st libaries
import turtle as t
import random
colors = ["orange", "green", "red", "purple", "blue"]
side = random.randint(10,500)
t.color(random.choice(colors))
t.shape("turtle")
t.fillcolor("blue")
t.begin_fill()
for x in range(1,4):
    t.forward(side)
    t.right(90)
    t.speed(2)
    t.shapesize(50)
t.end_fill()
for x in range(1,4):
    t.penup()
    t.goto(50,300)
    t.pendown()
    t.forward(side)
    t.right(90)
    t.speed(2)
    t.shapesize(50)

t.done()