#EH 1st turtle racing!
import random
import turtle as t
bruh = t.setup(700,700)
x_cord = 500
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

one.goto(-300,250)
two.goto(-300,125)
three.goto(-300,0)
four.goto(-300,-125)
five.goto(-300,-250)

one.pendown()
two.pendown()
three.pendown()
four.pendown()
five.pendown()

one.speed(3000)
two.speed(3000)
three.speed(3000)
four.speed(3000)
five.speed(3000)

one.speed(random.randint(1,5))
two.speed(random.randint(1,5))
three.speed(random.randint(1,5))
four.speed(random.randint(1,5))
five.speed(random.randint(1,5))

one.shape("turtle")
two.shape("turtle")
three.shape("turtle")
four.shape("turtle")
five.shape("turtle")

one.color("red")
two.color("green")
three.color("blue")
four.color("purple")
five.color("yellow")

line = t.Turtle()
line.penup()
line.goto(500,500)
line.pendown()
line.goto(500,-500)
line.penup()

for x in range(1,100):
    one.forward(random.randint(10,100))
    two.forward(random.randint(10,100))
    x2 = two.xcor()
    three.forward(random.randint(10,100))
    x3 = three.xcor()
    four.forward(random.randint(10,100))
    x4 = four.xcor()
    five.forward(random.randint(10,100))
    x5 = five.xcor()
    continue
t.end_fill()
while True:
    x1 = one.xcor()
    if x1 > x_cord:
        print("The red turtle has won")
        break