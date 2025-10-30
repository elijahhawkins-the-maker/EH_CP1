#EH 1st turtle racing!
import random
import turtle as t
x_cord = 500
t.setup(1500,1000)
t.bgcolor("black")
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

one.goto(-500,250)
two.goto(-500,125)
three.goto(-500,0)
four.goto(-500,-125)
five.goto(-500,-250)

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
line.color("white")
line.penup()
line.goto(500,500)
line.pendown()
line.goto(500,-500)
line.penup()
line.hideturtle()

for x in range(1,10000):
    one.forward(random.randint(10,100))
    x1 = one.xcor()
    if x1 >= 500:
        red = t.Turtle()
        red.color("red")
        red.penup()
        red.goto(-300,350)
        red.pendown()
        red.write("The red turtle wins!",font=("Arial",50,"normal"))
        red.hideturtle()
        break
    two.forward(random.randint(10,100))
    x2 = two.xcor()
    if x2 >= 500:
        green = t.Turtle()
        green.color("green")
        green.penup()
        green.goto(-300,350)
        green.pendown()
        green.write("The green turtle wins!",font=("Arial",50,"normal"))
        green.hideturtle()
        break
    three.forward(random.randint(10,100))
    x3 = three.xcor()
    if x3 >= 500:
        blue = t.Turtle()
        blue.color("blue")
        blue.penup()
        blue.goto(-300,350)
        blue.pendown()
        blue.write("The blue turtle wins!",font=("Arial",50,"normal"))
        blue.hideturtle()
        break
    four.forward(random.randint(10,100))
    x4 = four.xcor()
    if x4 >= 500:
        purple = t.Turtle()
        purple.color("purple")
        purple.penup()
        purple.goto(-300,350)
        purple.pendown()
        purple.write("The purple turtle wins!",font=("Arial",50,"normal"))
        purple.hideturtle()
        break
    five.forward(random.randint(10,100))
    x5 = five.xcor()
    if x5 >= 500:
        yellow = t.Turtle()
        yellow.color("yellow")
        yellow.penup()
        yellow.goto(-300,350)
        yellow.pendown()
        yellow.write("The yellow turtle wins!",font=("Arial",50,"normal"))
        yellow.hideturtle()
        break
t.end_fill()
t.done()