#EH 1st random maze generator
import random
import turtle as t
t.screensize(500,500)
t.bgcolor("black")

massive = []

line_maker = t.Turtle()
t.begin_fill()
line_maker.shape("turtle")
line_maker.color("red")
line_maker.penup()
line_maker.goto(400,400)
line_maker.pendown()
line_maker.goto(10,400)
line_maker.penup()
line_maker.goto(-10,400)
line_maker.pendown()
line_maker.goto(-400,400)
line_maker.goto(-400,-400)
line_maker.goto(-10,-400)
line_maker.penup()
line_maker.goto(10,-400)
line_maker.pendown()
line_maker.goto(400,-400)
line_maker.goto(400,400)
t.done()

