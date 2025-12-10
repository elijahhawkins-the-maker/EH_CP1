#EHCP1 DND!
import random as r
import time as t
import sys as s
def typing(text, delay=0.03):
    for char in text:
        s.stdout.write(char)
        s.stdout.flush()
        t.sleep(delay)
    print()
def roll(sides):
    return r.randint(1, sides)
p_damage = 0
m_damage = 0

start_weapons = {
"great axe":12,
"dagger":8,
"scimitar":10,
 "javelin":6, 
 "small dinky hammer":12
 }
typing("lore goes here...")
t.sleep(1.5)
typing("Welcome to the country of Draeburg, adventurer")
t.sleep(1.5)
typing("Before you start the quest of destroying the dragon king and his army,")
t.sleep(1.5)
typing("You must roll for your stats!")
t.sleep(1.5)
value = 0
value2 = 0
while value < 4:
    typing("rolling...")
    t.sleep(1.3)
    value += 1
while value2 <= 1:
    str = r.randint(5,20)
    dex = r.randint(5,20)
    con = r.randint(5,20)
    intt = r.randint(5,20)
    wis = r.randint(5,20)
    cha = r.randint(5,20)
    health = r.randint(1,20)
    ac = r.randint(5,20)
    typing(f"Your stats are...\n strength is {str}\n dexterity is {dex}\n constitution is {con}\n intelligence is {intt}\n wisdom is {wis}\n charisma is {cha}\narmor class is {ac}\n\n")
    if cha <= 15 or dex <= 15 or str <= 15 or con <= 15 or intt <= 15 or wis <= 15:
        re_roll = input("Do you want to roll your stats again, y or n?\n")
        if re_roll == "y":
            value2 += 1
            if value2 > 1:
                typing("Well well well, it seems you have reached your limit for rolling")
                break
            continue
        elif "n":
            break
        else:
            typing("not a valid input")
t.sleep(1.5)
typing("Now, here is the list of starter weapons, you can collect more as you go through the towns!")
t.sleep(1)
for key in start_weapons.keys():
    typing(key)
while True:
    s_weapon = input("Which of these weapons would you like?\n").lower()
    if s_weapon in start_weapons:
        value3 = start_weapons[s_weapon]
        typing(f"You have chosen {s_weapon}! nice!\n it does 1D{value3} damage!")
        break
    else:
        typing("Not an actual weapon")
t.sleep(1.5)
typing("Here is the list of towns you can go to!\n Belville\n Oxhall\n Coldham\n Madland\n Angousir\n Rockshield\n Spiritport\n Whitrock\n Frostpeaks\n or the capital, Drappes")
t.sleep(1.5)
choice = int(input("Now which town would you like to go to first, to start fighting the Dragon King's army!\n"))
"""---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
