import turtle
import random

def get_mid(p1, p2):
    """Finds the midpoint between two points."""
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

# Setup the turtle environment
t = turtle.Turtle()
screen = turtle.Screen()
screen.tracer(1)
t.fillcolor("red")
my_screen = turtle.Screen()
t.speed(0)
t.penup()
t.hideturtle()

# Define the three initial vertices
corners = [(0, 200), (-200, -100), (200, -100)]

# Start at an arbitrary point within the triangle
point = (random.randint(-100, 100), random.randint(-50, 100))

# Iterate and plot points
for i in range(100000000): # More iterations create more detail
    # Randomly choose a corner
    corner = random.choice(corners)
    
    # Calculate the midpoint between the current point and the chosen corner
    point = get_mid(point, corner)
    
    # Plot the new point
    t.goto(point)
    # Start plotting dots after a few initial iterations for better visual
    if i > 5: 
        t.pendown()
        t.dot(5) # You can adjust dot size
        t.penup()

# Keep the window open until clicked
my_screen.exitonclick()