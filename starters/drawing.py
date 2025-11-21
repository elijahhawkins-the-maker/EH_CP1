#EHCP1 Starter

import turtle as t

t.Turtle()
t.speed("fastest")
t.color("light blue")
t.penup()
t.goto(50,50)
t.pendown()

def draw(length):
    if length > 5:
        for i in range(3):
            t.forward(length)
            draw(length/3)
            t.backward(length)
            t.right(60)

for i in range(6):
    draw(100)
    t.right(60)
t.hideturtle()
t.done