#EHCP1 DND!
import random as r
import time as t
D100 = r.randint(1,100)
D20 = r.randint(1,20)
D12 = r.randint(1,12)
D10 = r.randint(1,10)
D6 = r.randint(1,6)
D4 = r.randint(1,4)
D2 = r.randint(1,2)
start_weapons = []
print("Welcome to the country of Draeburg, adventurer")
t.sleep(1.2)
print("Before you start the quest of destroying the dragon king and his army,")
t.sleep(1.2)
print("You must roll for your stats!")
value = 0
value2 = 0
while value < 4:
    print("rolling...")
    t.sleep(1.3)
    value += 1
while value2 <= 1:
    str = r.randint(1,20)
    dex = r.randint(1,20)
    con = r.randint(1,20)
    int = r.randint(1,20)
    wis = r.randint(1,20)
    cha = r.randint(1,20)
    health = r.randint(1,20)
    print(f"Your stats are...\n strength is {str}\n dexterity is {dex}\n constitution is {con}\n intelligence is {int}\n wisdom is {wis}\n charisma is {cha}\n\n")
    if cha <= 15 or dex <= 15 or str <= 15 or con <= 15 or int <= 15 or wis <= 15:
        re_roll = input("Do you want to roll your stats again, y or n?\n")
        if re_roll == "y":
            value2 += 1
            if value2 >= 1:
                print("Well well well, it seems you have reached your limit for rolling")
            continue
        elif "n":
            break
        else:
            print("not a valid input")