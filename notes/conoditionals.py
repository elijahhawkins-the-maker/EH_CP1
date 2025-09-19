#eh 1st conditionals 
import random
player_hp = 21
player_attack = 2
player_damage = 5
player_defense = 5

monster_hp = 15
monster_attack = 3
monster_damage = 10
monster_defense = 2

hit_roll = random.randint(1,20) + player_attack
damage_roll = random.randint(1,8) + player_damage
if hit_roll == 20:
    print("you got a major crit! you get to roll damage")
    damage_roll = random.randint(1,8) + random.randint(1,8) + player_damage
    print(f"you did {damage_roll-monster_defense} damage.")
    monster_hp -= (damage_roll-monster_defense)
elif hit_roll == 1:
    print("You rolled what I like to call... a skill issue")
    damage_roll = random.randint(1,12) + monster_damage
    player_hp -= (damage_roll - player_defense)
    print(f"the monster rolled {damage_roll}, your hp is now {player_hp}")
elif hit_roll + player_attack >= 12:
    print("you hit hard! roll for damage!")
    damage_roll = random.randint(1,8) + player_damage
    if damage_roll > monster_defense:
        print(f"you did {damage_roll-monster_defense} damage.")
        monster_hp -= (damage_roll-monster_defense)
    else:
        print("you did no damage")
else:
    print("you missed, skill issue.")

print("your turn is over")

if monster_hp > 0:
    attack_roll = random.randint(1,20) + monster_attack