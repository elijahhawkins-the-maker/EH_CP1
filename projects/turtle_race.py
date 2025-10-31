#EH 1st turtle racing!
#import random at the top of the code
import random
#import turtle and import it as t to make it easier to type in the functions
import turtle as t
#have the t.setup function to set the size of the screen to 1500*1000 pixels
t.setup(1500,1000)
#this makes the background color black to make it look much cooler and have much more contrast
t.bgcolor("black")
#this is assigning the turtles to the one-five variables
one = t.Turtle()
two = t.Turtle()
three = t.Turtle()
four = t.Turtle()
five = t.Turtle()
#this is the penup function that makes it so that the turtles don't draw while traveling
t.begin_fill()
one.penup()
two.penup()
three.penup()
four.penup()
five.penup()
#this function makes it so that the turtles go 3000 mph at first to get to their starting positions faster
one.speed(5000)
two.speed(5000)
three.speed(5000)
four.speed(5000)
five.speed(5000)
#this is the function that makes the turtles go to their starting positions
def position():
    one.goto(-725,250)
    two.goto(-725,125)
    three.goto(-725,0)
    four.goto(-725,-125)
    five.goto(-725,-250)
position()
#after the turtles go to their positions, this function makes it so that the turtles will start drawing again
one.pendown()
two.pendown()
three.pendown()
four.pendown()
five.pendown()
#this then makes the speed a random speed after the turtles have first started
def fast():
    one.speed(random.randint(1,5))
    two.speed(random.randint(1,5))
    three.speed(random.randint(1,5))
    four.speed(random.randint(1,5))
    five.speed(random.randint(1,5))
fast()
#this just makes the original pointers the shape of a turtle!
one.shape("turtle")
two.shape("turtle")
three.shape("turtle")
four.shape("turtle")
five.shape("turtle")
#this makes the size of the turtles bigger
one.shapesize(2)
two.shapesize(2)
three.shapesize(2)
four.shapesize(2)
five.shapesize(2)
#this function makes the color of the turtles different then black!
one.color("red")
two.color("green")
three.color("blue")
four.color("purple")
five.color("yellow")
#these sets of functions draw the line for the turtles to have to cross at 500 on the x axis
def finish():
    line = t.Turtle()
    line.color("white")
    line.penup()
    line.goto(500,500)
    line.pendown()
    line.goto(500,-500)
    line.penup()
    line.hideturtle()
finish()
#this is a for loop in a function that will make the turtles move continuously
def moving():
    for x in range(1,10000):
        one.forward(random.randint(10,100))
        #x1 is the variable assigned to the x cordinant of the turtle
        x1 = one.xcor()
        #if statement that checks if the x cord of the turtle is over 500 (aka where the line is)
        if x1 >= 500:
            #writing is assigned to a turtle
            red = t.Turtle()
            #this sets the color of the writing
            red.color("red")
            red.penup()
            #this function makes the font go to -300,500 cords
            red.goto(-300,350)
            red.pendown()
            #this function prints the text in arial that is 50 point size
            red.write("The red turtle wins!",font=("Arial",50,"normal"))
            #this hides the turtle after it writes
            red.hideturtle()
            #all of the rest of the if statements are the exact same, just use different variables to not mix up
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
moving()
#this is to end the turtles drawing lines
t.end_fill()
#this makes the window for the turtles stay open even after running the code
t.done()