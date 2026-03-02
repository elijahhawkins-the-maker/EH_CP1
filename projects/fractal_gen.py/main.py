#EHCP2 main menu

from fractal_funcs import choices

def main():
    print("Welcome to the sierpinski triangle generator!")
    while True:
        choice = input("Now, would you like to generate a cool fractal?\n y or n\n")
        if choice == "y":
            choices()
        elif choice == "y":
            break
        else:
            print("That ain't something you can do!")
main()