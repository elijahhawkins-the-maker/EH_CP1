#EH 1st funcs notes
#set variables
player_health = 100
monster_health = 100
#define functions
def damage(amount, turn):
    if turn == "player":
        return monster_health - amount, player_health
    else:
        return monster_health, player_health - amount
    
monster_health, player_health = damage(10, "player")
print(monster_health)
print(player_health)
def add(x,y):
    return x+y

total = add(5,5)
print(total)
print(f"10 + 72 = {add(10,72)}")
x = 0
while x < add(3,9):
    print("bruh")
    x += 1

print("bruuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuh")

def initials(name):
    names = name.split(" ")
    initials = ""
    for name in names:
        initials += name[0]

    return initials