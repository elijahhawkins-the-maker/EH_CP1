#EH 1st, dnd combat!
import random
name = input("What is your name?\n")
weapon = ["Great Axe","Musket","Spear","Morningstar","mini axe", "javelin"]
rare_weapon = "Wand of Wonder"
notdead = True
while notdead == True:
    health = 0
    f_skills = 0
    s_skills = 0
    e_skills = 0
    level = 1
    damage = 0
    character = int(input("What is the class that you would like?\n1 for barbarian\n2 for Wizard\n3 for fighter\n4 for engineer\n"))
    if character == 1:
        health += random.randint(5,20)
        f_skills += random.randint(5,20)
        weapon2 = random.choice(weapon)
    elif character == 2:
        health += random.randint(5,20)
        f_skills += random.randint(5,20) - 4
        s_skills += random.randint(5,20)
        weapon2 = random.choice(weapon)
    elif character == 3:
        health += random.randint(5,20)
        f_skills += random.randint(5,20)
        weapon2 = random.choice(weapon)
        if f_skills <= 16:
            f_skills + 4
    elif character == 4:
        health += random.randint(5,20)
        f_skills += random.randint(5,20)
        weapon2 = random.choice(weapon)
    else:
        print("Not a valid input my guy!")
    print(f"With this character, your health is {health}\nYour fighting skills are {f_skills}\nYour magic skills are {s_skills}\nAnd your weapon is {weapon2}")
    if weapon2 == "Great Axe":
        damage += 10