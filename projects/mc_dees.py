#EH 1st order up!
#import time to slow down the generation of the menu
import time as t
#this is the dictionary for main courses
main = {
    "burger":9.99,
    "nachos":11.99,
    "burrito":6.99,
    "extra crispy burrito":19.99,
    "taco special":15.99,
    "quesadilla":4.99,
    "taco burger":7.99,
    "gun shaped steak":99.99
}
#this is the dictionary for the sides and drinks on the menu
sides = {
    "fries":2.99,
    "extra chips":0.99,
    "small burrito":2.99,
    "small soda":0.99,
    "medium soda":1.99,
    "large soda":2.99,
    "extra large soda":3.99
}
#this is the tiny desert menu dictionary
des = {
    "ice cream":3.99,
    "bruh":9.99
}
#this prints a welcome message for the user
print("Welcome to McDees, where you always get the best food! What would you like?\n\n")
#this waits three seconds before it prints the menu
t.sleep(3)
#this is a for loop that prints out all of the items in the dictionary in a good way
print("These are the main courses!")
for key in main.keys():
    #prints the key, then the value of that key after it
    print(f"{key} is ${main[key]}")
#this separates the menus by 2 lines
#basically all of the rest of the for loops are the same but with the different dictionaries
print("\n\n")
t.sleep(3)
print("These are the sides and drinks!")
for key in sides.keys():
    print(f"{key} is ${sides[key]}")
print("\n\n")
t.sleep(3)
print("These are the desserts!")
for key in des.keys():
    print(f"{key} is ${des[key]}")
print("\n\n")
#a while loop that asks the user for the item they want
while True:
    #the input of the user with the lower() function that switches the input to lowercase
    bruh = input("Now what main course would you like?\n").lower()
    #if statement that checks whether the user actually put something that is in the menu
    if bruh in main:
        choice = main[bruh]
        #breaks the loop if the if statement is true
        break
    #else statement that tells the user that their choice isn't valid if it wasn't in the menu
    else:
        print("Not an item on the menu")
#all of the while loops are the same but with different variables and dictionaries
while True:
    bruh2 = input("Now what side would you like?\n").lower()
    if bruh2 in sides:
        choice2 = sides[bruh2]
        break
    else:
        print("Your choice is not on the menu")
while True:
    bruh3 = input("Now what is your second side?\n")
    if bruh3 in sides:
        choice3 = sides[bruh3]
        break
    else:
        print("Your choice is not on the menu")
while True:
    bruh4 = input("Now what dessert would you like?\n").lower()
    if bruh4 in des:
        choice4 = des[bruh4]
        break
    else:
        print("Your choice is not on the menu")
#this adds all of the choice's pices together for the total
total = main[bruh] + sides[bruh2] + sides[bruh3] + des[bruh4]
#this set of print statements shows what they ordered and the final price
print(f"Your main course is {bruh} and it is ${choice}")
print(f"Your side dish is {bruh2} and it is ${choice2}")
print(f"Your second side is {bruh3} and it is ${choice3}")
print(f"Your dessert is {bruh4} and it is ${choice4}")
print(f"Your total is ${total} with all of these items")