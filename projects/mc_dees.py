#EH 1st order up!
import time as t
choices = []

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

sides = {
    "fries":2.99,
    "extra chips":0.99,
    "small burrito":1.99,
    "small soda":0.99,
    "medium soda":1.99,
    "large soda":2.99,
    "extra large_soda":3.99
}
des = {
    "ice cream":3.99,
    "bruh":9.99
}
print("Welcome to McDees, where you always get the best food! What would you like?\n\n")
t.sleep(3)
print("These are the main courses!")
for key in main.keys():
    print(f"{key} is {main[key]}")
print("\n\n")
t.sleep(3)
print("These are the sides!")
for key in sides.keys():
    print(f"{key} is {sides[key]}")
print("\n\n")
t.sleep(3)
print("These are the desserts!")
for key in des.keys():
    print(f"{key} is {des[key]}")
print("\n\n")
while True:
    bruh = input("Now what main course would you like?\n").lower()
    if bruh in main:
        choice = main[bruh]
        break
    elif bruh == "none":
        break
    else:
        print("Not an item on the menu")
while True:
    bruh2 = input("Now what side would you like?\n").lower()
    if bruh2 in sides:
        choice2 = sides[bruh2]
        break
    elif bruh == "none":
        break
    else:
        print("Your choice is not on the menu")
while True:
    bruh3 = input("Now what dessert would you like?\n").lower()
    if bruh3 in des:
        choice3 = des[bruh3]
        break
    elif bruh == "none":
        break
    else:
        print("Your choice is not on the menu")
total = main[bruh] + sides[bruh2] + des[bruh3]
print(f"Your main course is {bruh} and it is ${choice}")
print(f"Your side dish is {bruh2} and it is ${choice2}")
print(f"Your dessert is {bruh3} and it is ${choice3}")
print(f"Your total is {total} with all of these items")