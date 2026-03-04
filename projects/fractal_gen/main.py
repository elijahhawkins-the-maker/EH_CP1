#EHCP2 main menu
import turtle as t

def choices():

    screen = t.Screen()

    color = screen.textinput("Color", "What is the color that you would like the triangle to be?\n").strip().lower()
    back = screen.textinput("Background", "Now what is the background color that you would like it to be?\n").strip().lower()
    depth = screen.numinput("Depth", "What is the depth that you want the fractal to have (1-9)?\n")
    from fractal_funcs import run
    run(int(depth), back, color)
    screen.update()

def main():
    print("Welcome to the sierpinski triangle generator!")
    while True:
        choice = input("Now, would you like to generate a cool fractal?\n y or n\n")
        if choice == "y":
            choices()
        elif choice == "n":
            break
        else:
            print("That ain't something you can do!")
main()