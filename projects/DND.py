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

def combat(m_health, m_damage, health, gold_given):
    global gold
    typing("Now you are fighting your opponent")
    damage = value3
    while True:
        atk = input("What would you like to do?\n Use a heal potion\n attack,\n or flee?\n").lower()
        if atk == "attack":
            show_inventory()
            hit = input("Alrighty, what would you like to use in your inventory to attack?\n").lower()
            if hit in inventory and start_weapons or rare_weapons or exotic_weapons or secret_weapons or spells:
                user = inventory[hit]
                typing(f"You chose to use {hit}!")
                typing(f"You did {user} damage!")
                m_health -= user
        elif atk == "heal potion":
            if "heal potion" in inventory:
                typing(f"You healed 80% of your health! Also potentially gained some!")
                health *= 1.60
            else:
                typing("You don't have a healing potion")
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
            typing("You died! You lose some gold!")
            if gold <= gold_given:
                gold -= gold
            elif gold > gold_given:
                gold -= gold_given
            break
        if m_health <= 0:
            typing(f"You won against your opponent! You gain {gold_given} gold!")
            gold += gold_given
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
        combat(30,r.randint(1,10),35,30)
        t.sleep(1.5)
        typing("That was a close one... But you ended up making it out of the town!")
        t.sleep(1.5)
        choice2 = input("Now that you have beaten the easiet general out of the rest, it is time that you choose the next town to go to!\n")
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
        typing("But just as you thought you were good, you run into one of the military generals of the Dragon King!")
        combat(30,r.randint(1,10),35,30)
def madland():
    global gold
    gold *= 2
    typing("You've traveled long and far to this town, but it looks so different compared to any other places...")
    t.sleep(1.5)
    typing("It looks poor and there is no fully built houses any where you look")
    t.sleep(1.5)
    typing("Then you realize, you're in the town of the poor in Draeburg.")
    t.sleep(1.5)
    while True:
        path = input("Now what would you like to do in the town of madland?\n'give' for giving gold to someone homeless,\n'shop' for going to a shop to see what they have\n or 'fight' for fighting a homeless guy\n").lower().strip()
        if path == "give":
            gift = int(input(f"So you have chosen to give some gold to the homeless, how much would you like to give out of {gold}\n"))
            if gift == 0:
                typing("Wooooow...")
                t.sleep(1.5)
                typing("You gave no gold! Why did you even pick generousity in the first place?")
            elif gift == 1:
                typing("Okay...")
                t.sleep(1.5)
                typing("You only gave 1 gold! Honestly it's good enough.")
                t.sleep(1.5)
                typing("But still, with inflation these days, what is 1 gold gonna get ya!?")
                t.sleep(1.5)
                typing("Hey at least they still appreciate it")
                break
                gold -= 1
                break
            elif gift > 1 and gift <= 10:
                typing("Alrighty the generousity is getting there...")
                t.sleep(1.5)
                typing("Well the homeless definitely thank you for your charitable-ness")
                t.sleep(1.5)
                gold -= gift
                break
            elif gift > 10:
                typing(f"Nice! You gave {gift} gold to the homeless, not too bad!")
                t.sleep(1.5)
                typing("Because of the generousity that you have, in return they give you a rare weapon of your choice!")
                for x in rare_weapons:
                    print(x)
                typing("Those are your choices to chose from")
                t.sleep(1.5)
                w_choice = input("Now what weapon would you like to choose?").lower()
                if w_choice in rare_weapons:
                    chosen_item = rare_weapons[w_choice]
                    inventory[w_choice] = chosen_item
                    typing(f"You officially now have {w_choice}!")
                    t.sleep(1.5)
                    typing("... and that is because of your generousity")
                    break
            elif gift > gold:
                typing("You can't give that much!")
            else:
                typing("You can't give that!")
        elif path == "shop":
            typing("You walk to a shop in the middle of the delapidated town...")
            t.sleep(1.5)
            typing("You walk into the rundown store...")
            shop()
            break
        elif path == "fight":
            typing("So you happen to chose fighting a homeless person")
            t.sleep(1.5)
            typing("Why though?")
            t.sleep(1.5)
            typing("Little do you know, this fighting won't be as easy as you thought...")
            combat(50,r.randint(1,18),35,1)
            typing("Seriously why did you think to do that")
            t.sleep("Anyway...")
        else:
            typing("You can't do that!")
    typing("Whichever one you did, after you did it, you decide to walk down the main street of this town...")
    t.sleep(1.5)
    typing("You suddenly wonder why this town is so rundown")
    t.sleep(1.5)
    typing("But then you see something in the distance")
    t.sleep(1.5)
    typing("It's a general that has heard about you before!")
    t.sleep(1.5)
    typing("He starts to run at you at break-neck speeds, like you've never seen...")
    t.sleep(1.5)
    typing("You start to run, hoping you can escape the inevitable")
    t.sleep(1.5)
    typing("He continues to catch up, and you pray that he doesn't get you")
    t.sleep(1.5)
    typing("Just as he is about to reach you, you do some crazy parkour")
    t.sleep(1.5)
    typing("But he ends up grabbing you in the end, due to him being super tall..")
    t.sleep(1.5)
    typing("Now, all you have left to do is fight.")
    combat(35,r.randint(1,18),25,40)
    t.sleep(1.5)
    typing("Whether you beat him or not, you continue to the next town...")
    gold /= 2
    round(gold)
    t_choice = input("Now which town do you want to go to?")
def Angousir():
    typing("You walked a long way to get to this town, and this town looks...")
    t.sleep(1.5)
    typing("Very nice oddly")
    t.sleep(1.5)
    typing("As you're looking around some more, you realize...")
    t.sleep(1.5)
    typing("This is the rich town!")
    t.sleep(1.5)
    a_choice = input("What would you like to do in this town?\n'break' for breaking into a mansion\n'shop' to buy somethin\n'grafetti' for vandalizing someone's mansion\n or 'look' to dream about some nice homes").lower()
    while True:
        if a_choice == "break":
            typing("So you decide to break into someone's house?")
            t.sleep(1.5)
            typing("Sounds wrong since you're trying to save a country but alrighty")
            t.sleep(1.5)
            typing("So you break a window...")
            t.sleep(1.5)
            typing("Then you step into the huge place")
            t.sleep(1.5)
            typing("Then almost instantly, you hear an ear piercing alarm sound that...")
            t.sleep(1.5)
            typing("Echos throughout the entire town!")
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
"wind":12,
"heal potion":10
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
typing("Here is the list of towns you can go to!\n Belville\n Madland\n Angousir\n Rockshield\n Spiritport\n Whitrock\n Frostpeaks\n or the capital, Drappes")
t.sleep(1.5)
while True:
    choice = input("Now which town would you like to go to first, to start fighting the Dragon King's army!\n")
    if choice == "Belville":
        belville()
        break
    elif choice == "Madland":
        madland()
        break
    else:
        typing("Not a town on the map it seems...")
"""---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""