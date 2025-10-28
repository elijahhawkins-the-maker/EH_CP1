#EH 1st, dnd combat! (sort of)
import random
name = input("What is your name?\n")
weapon = ["Great Axe","Musket","Spear","Morningstar","mini axe", "javelin"]
alive = True
health = 0
damage = 0
a_class = 0
monster_h = 50
weapon2 = random.choice(weapon)
character = int(input("What is the class that you would like?\n1 for barbarian\n2 for Wizard\n3 for fighter\n4 for engineer\n"))
if character == 1:
    health += random.randint(5,20)
    a_class += random.randint(10,20)
elif character == 2:
    health += random.randint(5,20)
    a_class += random.randint(5,15)
elif character == 3:
    health += random.randint(5,20)
    a_class += random.randint(10,20)
elif character == 4:
    health += random.randint(5,20)
    a_class += random.randint(10,20)
else:
    print("invalid input buddy")
print(f"With this character, your health is {health}\nYour armor class is {a_class}\nAnd your weapon is {weapon2}")
if weapon2 == "Great Axe":
    damage += 12
elif weapon2 == "Musket":
    damage += 10
elif weapon2 == "Spear":
    damage += 7
elif weapon2 == "Morningstar":
    damage += 8
elif weapon2 == "mini axe":
    damage += 6
elif weapon2 == "javelin":
    damage += 7
else:
    print("huh! you broke the code somehow!")
print(f"With your weapon, {weapon2}, you do {damage} damage to anything you attack!\n\n")
print(f"Now, in your supposed campaign, you're just casually walking... then suddenly the Goblin King challenges you to a fight!\n\n")
print("Now it is time to roll for initiative!")
initiative = random.randint(1,20)
if character == 1:
    rage = input("Would you like to initiate a rage?\nif you do, type yes. It will result in a small health disadvantage!\nBut you will gain more damage!\n")
    if rage == "yes":
        health -= 3
        damage += 3
    else:
        pass
else:
    pass
while True:
    def p_attack():
        global damage
        global health
        global monster_h
        attack = random.randint(1,20)
        if initiative >= 10:
            print("You rolled high enough! Now you shall attack!")
            if attack <= 8:
                print("You did not hit! It is now the Goblin King's turn!")
            elif attack >= 9:
                print("You did hit!")
                monster_h -= damage
                print(f"You did {damage} damage! Now the Goblin King gets his turn!")
        else:
            print("You rolled too low! You do not attack\n\n")
        print(f"After that, the health of the Goblin King is {monster_h}!")
    p_attack()
    def m_attack():
        global m_damage
        global health
        m_damage = random.randint(1,12)
        print("Now the Goblin King is going to attack you! You might be cooked fella!")
        m_roll = random.randint(1,20)
        if m_roll >= a_class:
            print(f"The Goblin King hits you! You take {m_damage} damage from him!\nYour health is now {health}")
            health -= m_damage
        else:
            print("He missed! What a miracle for you! For now...")
    again = int(input("Would you like to try and hit him again?\nType 1 if yes\n"))
    if monster_h <= 0:
        print("You won against the Goblin King!")
        break
    elif health <= 0:
        print("You died before you could kill the Goblin King!")
        break
    m_attack()
    if again == 1:
        continue
    else:
        break