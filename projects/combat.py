#EH 1st, dnd combat!
import random
health2 = r"[1-20]"
Chance = r"[1-1000000]"
while True:
    def stats(hit_dice, health, armor_class, creatures, atk_bonus):
        stat = {
            atk_bonus:0,
            hit_dice:0,
            health:0,
            armor_class:0,
            "dead":False
        }
        name = input("What is your name?\n")
        creatures = ["Buff Goblin", "You"]

    def user(usr, atk, weapon):
        weapon = input("What do you want as your weapon?\n You can choose:\nGreat Axe\nSpear\nMusket\or Morningstar")
        atk = random.randint(health2)