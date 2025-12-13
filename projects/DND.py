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
gold = 50
inventory = {}
def show_inventory():
    print("These are your items!")
    for item in inventory.keys():
        typing(item)

def combat(m_health, m_damage, health):
    global gold
    typing("Now you are fighting your opponent")
    damage = value3
    while True:
        atk = input("What would you like to do?\n Use a heal potion\n attack,\n or flee?").lower()
        if atk == "attack":
            show_inventory()
            hit = input("Alrighty, what would you like to use in your inventory to attack?").lower()
            if hit in inventory and start_weapons or rare_weapons or exotic_weapons or secret_weapons or spells:
                user = inventory[hit]
                typing(f"You chose to use {hit}!")
                typing(f"You did {user} damage!")
                m_health -= user
        elif atk == "heal potion":
            if "heal potion" in inventory:
                typing(f"You healed 80% of your health! Also potentially gained some!")
            else:
                typing("You don't have a healing potion")
                health *= 1.80
        elif atk == "flee":
            typing("You successfully fleed!")
            break
        else:
            typing("You can't fight with that!")
        typing("Now it is the opponent's turn!")
        mon_attempt = r.randint(5,20)
        m_hit = r.randint(1,10)
        if mon_attempt >= ac:
            typing(f"You took {m_hit} damage!")
            health -= m_hit
            typing(f"Your health is now {health}")
        else:
            typing("Your opponent did not hit!")
        if health <= 0:
            typing("You died! You do not get any gold!")
            break
        if m_health <= 0:
            typing("You won against your opponent! You gain 30 gold!")
            gold += 30
            break

def belville():
    global gold
    typing("After a long trek, you finally make your way to Belville, a once normal looking town has turned to something... deserted and destroyed.")
    t.sleep(0.5)
    typing("You hear someone come up behind, you get scared, thinking of the worst, when you turn around...")
    t.sleep(1.5)
    typing("It's just a dealer, but he seems to have something good in his wagon...")
    shop()
    t.sleep(1.5)
    typing("Whether you bought something or not, you go to explore the rest of Belville!")
    while True:
        try:
            act_choice = int(input("What do you want to do?\n1 for going into an abandoned house\n2 for going into a desolate basketball court\n"))
            break
        except ValueError:
            typing("That isn't something you can do!")
    if act_choice == 1:
        typing("You go into the abandoned house...")
        t.sleep(1.5)
        typing("You see a bunch of dusty pictures on the wall, along with destroyed furniture")
        t.sleep(1.5)
        typing("You wonder, why would the Dragon King ever cause something like this to happen to people...")
        t.sleep(1.5)
        typing("Anyways you continue through to the second floor of the house")
        t.sleep(1.5)
        typing("... and you fall through the floor!")
        t.sleep(1.5)
        typing("Luckily you landed on a half broken couch")
        t.sleep(1.5)
        typing("After that, you decide to go out of the house...")
        t.sleep(1.5)
        typing("But when you come out of the house... you run into one of the Dragon King's military generals!")
        combat(30,r.randint(1,10),35)

    elif act_choice == 2:
        typing("You go into the basketball court, to find an almost fully inflated basketball!")
        t.sleep(1.5)
        typing("You go to shoot into the hoop, you actually make it from across the court!")
        t.sleep(1.5)
        typing("Because of that, you get gold for that fire trickshot!")
        gold += 5
        t.sleep(1.5)
        typing("After the crazy trick that you just did, you venture out of the basketball court")
        typing("... eager to beat the Dragon King once and for all of the country of Draeburg!")
        t.sleep(1.5)
        typing("But just as you thought you were good, you run into one of the military generals!")
        combat(30,r.randint(1,10),35)
start_weapons = {
"great axe":12,
"dagger":8,
"scimitar":10,
"javelin":6, 
"small dinky hammer":12
}
rare_weapons = {
"long sword":15,
"pickaxe":12,
"musket":10,
"lightning bolt":15,
}
exotic_weapons = {
"random cloth":20,
"big dinky hammer":14,
"signature sledge":20,
"plastic knife":16,
"get outa here":25
}
secret_weapons = {
"soda cup":30,
"wand of wander":100,
"555 dc motor":50,
"whip of the century":25,
"mega knight":80,
"Ms LaRose":200
}
spells = {
"freeze":10,
"fire":15,
"earthquake":20,
"levitation":12,
"thin air":13,
"tornado":20,
"drown":17,
"electrocution":18,
"riches":10,
"insanity":8,
"rage attack":9,
"wind":12
}

starter_weapons = list(start_weapons.keys())
rarer_weapons = list(rare_weapons.keys())
spellers = list(spells.keys())
def shop():
    global gold
    shop_list = [r.choice(starter_weapons), r.choice(spellers), r.choice(rarer_weapons)]
    typing("You take a look to see what they have...")
    for x in shop_list:
        typing(x)
    buy = input("What item would you like to buy? \nor type n to not buy anything\n")
    while True:
        if buy in shop_list and start_weapons or rare_weapons or spells:
            if buy in start_weapons:
                bought_item = start_weapons[buy]
                if bought_item >= gold:
                    typing("This costs too much")
                elif bought_item <= gold:
                    inventory[buy] = bought_item
                    gold -= bought_item
                    typing(f"You have bought {buy}! You loose {bought_item} gold!")
                    break
            elif buy in rare_weapons:
                bought_item = rare_weapons[buy]
                if bought_item >= gold:
                    typing("This costs too much")
                elif bought_item <= gold:
                    inventory[buy] = bought_item
                    gold -= bought_item
                    typing(f"You have bought {buy}! You loose {bought_item} gold!")
                    break
            elif buy in spells:
                bought_item = spells[buy]
                if bought_item >= gold:
                    typing("This costs too much")
                elif bought_item <= gold:
                    inventory[buy] = bought_item
                    gold -= bought_item
                    typing(f"You have bought {buy}! You loose {bought_item} gold!")
                    break
        elif buy == "n":
            break
        else:
            typing("Not an item")
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
health = 0
while value < 4:
    typing("rolling...")
    t.sleep(1.3)
    value += 1
while value2 <= 1:
    strr = r.randint(5,20)
    dex = r.randint(5,20)
    con = r.randint(5,20)
    intt = r.randint(5,20)
    wis = r.randint(5,20)
    cha = r.randint(5,20)
    ac = r.randint(5,15)
    typing(f"Your stats are...\n strength is {strr}\n dexterity is {dex}\n constitution is {con}\n intelligence is {intt}\n wisdom is {wis}\n charisma is {cha}\narmor class is {ac}\n\n")
    if cha <= 15 or dex <= 15 or strr <= 15 or con <= 15 or intt <= 15 or wis <= 15:
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
        inventory[s_weapon] = value3
        break
    else:
        typing("Not an actual weapon")
t.sleep(1.5)
typing("Here is the list of towns you can go to!\n Belville\n Oxhall\n Coldham\n Madland\n Angousir\n Rockshield\n Spiritport\n Whitrock\n Frostpeaks\n or the capital, Drappes")
t.sleep(1.5)
while True:
    choice = input("Now which town would you like to go to first, to start fighting the Dragon King's army!\n")
    if choice == "Belville":
        belville()
        break
    else:
        typing("Not a town on the map it seems...")
"""---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""