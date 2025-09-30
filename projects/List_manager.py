# EH 1st Shopping List Manager
run = True

items = []

while run:
    print("what would you like to do to your shopping list\n 1: add something\n 2: remove something\n 3: show the list\n 4: leave the code")
    a = int(input("input the number below:\n"))

    if a == 1:
        item = input("what would you like to add to the list?\n")
        items.append(item)

    elif a == 2:
        de_itemize = input("what item do you want to remove?\n")
        index = items.index(de_itemize)
        items.pop(index)

    elif a == 3:
        print(f"this is the items in your list:\n {items}")

    elif a == 4:
        run = False

    else:
        print("not valid input loser")

print(items)