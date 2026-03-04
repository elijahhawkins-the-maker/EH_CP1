#EHCP2 main menu
#import turtle at the top as t
import turtle as t
#this is the function that asks the user for the parameters of the sierpinski triangle
def choices():

    screen = t.Screen()
    #uses a special type of input that shows up on the turtle screen
    color = screen.textinput("Color", "What is the color that you would like the triangle to be?\n").strip().lower()
    back = screen.textinput("Background", "Now what is the background color that you would like it to be?\n").strip().lower()
    depth = screen.numinput("Depth", "What is the depth that you want the fractal to have (1-9)?\n")
    #imports the function right here so it doesn't run early
    from fractal_funcs import run
    #runs the sierpinski triangle code
    run(int(depth), back, color)
    screen.update()

def main():
    #welcomes the user to the generator
    print("Welcome to the sierpinski triangle generator!")
    #While loop for idiot proofing
    while True:
        choice = input("Now, would you like to generate a cool fractal?\n y or n\n")
        #if statements that check whether they want to generate one or not
        if choice == "y":
            choices()
        elif choice == "n":
            break
        else:
            print("That ain't something you can do!")
main()