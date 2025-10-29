#EH 1st turtle racing!
import random
import turtle as t

one = t.Turtle()
two = t.Turtle()
three = t.Turtle()
four = t.Turtle()
five = t.Turtle()

t.begin_fill()
one.penup()
two.penup()
three.penup()
four.penup()
five.penup()

one.goto(0,200)
two.goto(0,100)
three.goto(0,0)
four.goto(0,-100)
five.goto(0,-200)

one.pendown()
two.pendown()
three.pendown()
four.pendown()
five.pendown()

one.speed(random.randint(1,5))
two.speed(random.randint(1,5))
three.speed(random.randint(1,5))
four.speed(random.randint(1,5))
five.speed(random.randint(1,5))

for x in range(5):
    break
t.end_fill()

t.done()