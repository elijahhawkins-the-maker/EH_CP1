#EHCP2 main menu

def choices():
    color = input("What is the color that you would like the triangle to be?\n").lower()
    background = input("Now what is the background color that you would like it to be?\n").lower()
    return background, color

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