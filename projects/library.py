#EHCP2
#importing time for delay between print statements
import time as t
#original empty list that things will get added to
library = []
def add():
    usr = input("What do you want to add to your library?\n Please type title and author of book\n").lower()
    library.append(usr)
    print(f"You have added '{usr}' to your library")
    #return menu() at the end of every function to exit and return to menu
    return menu()
#this function removes the item from the list with the remove function
def remov():
    while True:
        for x in library:
            print(x)
        usr = input("This is what you have!\n what would you like to remove?\nType n to stop removing\n").lower()
        #some quality idiot proofing with if statements
        if usr in library:
            library.remove(usr)
            break
        elif usr == "n":
            return menu()
        else:
            print("That ain't in your library!")
#uses a for loop to effectively search through and find matches through only one word
def search():
    while True:
        usr = input("What is the item you would like to search for?\n Type in author's first name or first word in book title\n").strip().lower()
        items = [x for x in library if usr in x]
        #converts found items into a list
        if items:
            print("Matches have been found!")
            for i in items:
                print(i)
            return menu()
        else:
            print("No matches to your search were found!")
            return menu()

def view():
    print("These are your items")
    #converts the list to a tuple
    lib2 = tuple(library)
    #for loop to display items
    for x in lib2:
        print(x)
    t.sleep(3)
    return menu()
#main menu function with if statements in a while loop and a try-except statement for idiot proofing
def menu():
    print("Welcome to YOUR personal library!")
    while True:
        try:
            usr = int(input("What would you like to do?\n 1 for adding to it (do this first if you have nothing in it!)\n 2 for removing something from it\n 3 for finding something in it\n 4 for displaying it\n5 for being done\n"))
            if usr == 1:
                add()
                break
            if usr == 2:
                remov()
                break
            if usr == 3:
                search()
                break
            if usr == 4:
                view()
                break
            if usr == 5:
                return
            else:
                print("That ain't something you can do!")
        except ValueError:
            print("You need to enter a number!")
menu()

