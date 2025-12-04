#EHCP1 DND final pseudocode
#import random as r
#import time as t for time between print statements
#a print statement that welcomes the adventurer to the country of Draeburg
"""-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
#variables:
#list with the classes in it
#list with weapons in it
#value = 0
#gold will equal 50 to start with
#level will equal 1 at first
#list for the inventory
#heal will equal false
#health
#max health
"""-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
#while loop that only executes when the value is under 2
    #input that allows them to choose classes for their character such as barbarian, sorcerer, and more
    #another input for weapons
    #strength = random integer from 1 to 20
    #dexterity = random integer from 1 to 20
    #constitution = random integer from 1 to 20
    #intelligence = random integer from 1 to 20
    #wisdom = random integer from 1 to 20
    #charisma = random integer from 1 to 20
    #health = random integer from 1 to 20
    #if statements that check whether they are in a certain number range, then if it is in that number range, it gives a modifier
    #more if statements for 
    #another user input that asks if they want to roll their stats again
    #value + 1 to make it so that the while loop can execute one more time
    #once value reaches 2, the loop breaks
"""-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
#functions time!
#there will be a function for each town, having slight stat changes over each like 
#there will be a function for combat which will look like this:
#define combat(health, opponent_health, weapon, and much more)
    #monster hp will get defined
    #player health will go down or added depending on level and healing potions, healing potions will be defined later
#print statement that tells the user that they arrived at the first town, Belville
#yet another function for the shops in the cities, they will mostly have the same stuff, with some small diffs between them
#a function will be set for the shop in the poor city and the rich city because of the gold being worth double or half
#then after all this will be some of the print statements that will tell the user what to do and also the many inputs that will be put for the shops and other things
"""-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
#what shop functions will look like:
    #list for the items in the shop, either that or a dictionary with the prices
    #print statement will be in a for loop
    #print statement for the items in the shop
    #time delay in between print statements using the 
    #there will be a user input for the shop items
    #conditional that will check whether a item that the user chooses is in the shop (list or dictionary, which ever works better)
"""----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
#healing function!
    #once the user gets a healing potion in their inventory, and they use it, there will be a while loop that will loop and add more health until the potion adds 10 more health, or reaches max health
    #input for the use of the healing potion
    #while loop will look like this:
        #adds 1 to health every time it loops
        #conditional for if the health reaches max or health + 10
            #then it breaks once it does
"""----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
#boss function:
    #will be like combat function but being more hard like stronger attacks and more spells being casted
    #health will be taken down 1.50x as much because the Dragon King is stronger!
"""----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
#Weapons!
    #variable for damage will be set to 0
    #the variable will have a number added to it once the user chooses their weapon
    #conditionals for the choosing of the weapons
    #here is a list of the starter weapons:
        #Great axe: 1D12 damage (will be determined through a random integer for the dice)
        #Javelin: 1D8 damage
        #Long sword: 1D10 damage
        #Great sword: 1D12 damage
        #sledge hammer: 1D20 damage, but very slow
    #Rare and rarer weapons:
        #Piece of cloth 2D20
        #Poison potion: 1D12, can be thrown from afar
        #thats it with rares weapons for now
    #Secret weapons:
        #Wand of Wander
        #Thats it for now
"""--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
#Spells!
    #a second variable for the spell damage that will have no value until the user chooses a spell
    #an input for the spell choosing
    #a list of spells
    #here is the list:
        #Potion of freezing: 1D8 damage (will only be available in Frostpeaks), rare
        #Zap of electricity: 1D12 damage, exotic
        #Stinking cloud: 1D6 damage, secret
        #Fireball: 1D10 damage, uncommon
        #That's all for now
"""--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
#Cities (functions):
    #defining all of the cities as functions
        #defining the city Belville:
            #