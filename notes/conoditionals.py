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

if hit_roll > 12:
    print("you hit hard! roll for damage!")
    damage_roll = random.randint(1,8) + player_damage
    if damage_roll > monster_defense:
        print(f"you did {damage_roll-monster_defense} damage.")
        monster_hp -= (damage_roll-monster_defense)
    else:
        print("you did no damage")
else:
    print("you missed, skill issue.")