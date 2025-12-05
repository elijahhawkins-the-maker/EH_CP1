#EHCP1 DND final pseudocode
#import random as r
#import time as t for time between print statements
#a print statement that welcomes the adventurer to the country of Draeburg
"""-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
#variables:
#list with the classes in it
#list with weapons in it
#list with spells
#main lists with possible items in shops
#value is 0
#gold will equal 50 to start with
#level will equal 1 at first
#list for the inventory
#heal will equal false
#health
#max health
#XP is 0 for now
#probably many more unplanned variables to come
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
    #once value reaches 2, the loop breaks with a break statement
"""-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
#how you start the game and how it runs!
    #there will be an input where you will choose the town after you roll for stats
    #a print statement with the difficulty of the town (will be numbered from 1 to 10)
    #a list with the functions of the cities
    #then there will be a set of conditionals that will check if the city of your choosing is in the list
    #an input that says "are you sure you want to go there" if the difficulty is over 5
    #more conditionals for whether the user says yes or no
    #once the town is chosen, the function for that town will execute
    #once you reach the end of the town, there will be another input for choosing the town you want to go to again with the same set of conditions
"""-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
#functions time!
#there will be a function for each town, having slight stat changes over each like 
#there will be a function for combat which will look like this:
#define combat function health, opponents health, weapon, and much more
    #monster hp will get defined
    #player health will go down or added depending on level and healing potions, healing potions will be defined later
    #will gain XP after each battle win, which will eventually increase level
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
    #there will be an input for possible negotiation
    #random integer between 0 and 1 for whether seller accepts the offer, will be more likely to reject, the lower the offer
    #conditionals for whether new offer gets accepted, as the value gets lower in comparison to the item, the chance goes down
"""----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
#healing function!
    #once the user gets a healing potion in their inventory, and they use it, there will be a while loop that will loop and add more health until the potion adds 10 more health, or reaches max health
    #input for the use of the healing potion
    #while loop will look like this:
        #adds 1 to health every time it loops
        #conditional for if the health reaches max or health + 10
            #then it breaks once it does
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
    #all these weapons below will come from chests, every chest will be a list
    #Rare and rarer weapons:
        #Piece of cloth 2D20
        #Poison potion: 1D12, can be thrown from afar
        #thats it with rare weapons for now
    #Secret weapons:
        #Wand of Wonder: can cast anything inside of the spells list randomly
        #The Wand of the Chosen: Like wand of wonder but you can choose any spell to cast
        #The Spear of Decay: 1D100, will be one of the most powerful items in the game, extremely hard to get
        #Thats it for now (they are secret for a reason! Some of them can't be known at all.)
"""--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
#Spells!
    #a second variable for the spell damage that will have no value until the user chooses a spell
    #an input for the spell choosing
    #a list for the spells
    #here is the list:
        #Potion of freezing: 1D8 damage (will only be available in Frostpeaks), rare
        #Zap of electricity: 1D12 damage, exotic
        #Stinking cloud: 1D6 damage, secret
        #Fireball: 1D10 damage, uncommon
        #strength potion: increases user strength permenently, epic
        #speed potion: increases user speed permanently, epic
        #That's all for now
"""--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
#Cities (functions):
    #defining all of the cities as functions
        #general overview of city function:
            #will be in a while loop for going back in rooms and houses in the town
            #variable will be set for if a chest exists
            #list of possible items in chest
            #random choice function for choosing something in the list to have in the chest
            #conditonal for the chest variable, if it equals 1, everything inside of the list for the chest goes away
            #try and except statement for if there is items in the chest list, if there isn't, it gives you a disapointing print statement that says there is nothing there :)
            #at the end of the loop, the chest variable value becomes 1, deleting it from the room permanently
            #shop function will go somewhere in the functions, random each time
            #list for the items in the shops, maybe a dictionary if assigning prices
            #input for a choice of houses and rooms for the user
            #list of places in said town
            #conditional for if the user choice is in the list
            #after they have explored everything, the user will come across an military general, that they will have to fight
            #combat function will go here for fighting the general
            #an item will drop that will automatically add to their inventory list
    #difference in functions
        #regular towns with some small diffs
            #Belville
            #Oxhall
            #Coldham
        #Madland (poor area)
            #Value of gold gets doubled due to everyone using copper pieces in this town
            #more combat happens due to increase in robbery
        #Angousir (rich area)
            #value of gold gets cut in half, due to everyone using platinum pieces here
            #if you get hold of platinum pieces, you gain charisma in every other town you go to, allowing for easier negotiation and easier to buy stuff
            #can offer platinum pieces to the military generals, but it will effect the final ending
        #Rockshield (military town)
            #security will be extra high here, you have to roll for stealth for every move
            #very good loot and weapons located here, that's why it is high security
            #list for rarer weapons
            #if the guards catch you, you go to battle, and if you lose, you don't die, but get thrown out of the town and lose the opportunity for loot entirely
            #the guards catching you will be based on a conditional of you rolling a 5 or lower with stealth (these guards are very bad and untrained)
            #it will be fairly easy to fight the guards in most cases
        #Spiritport (religious area)
            #this will be the only town with spells, but they have poorer weapons here
            #list for terrible weapons
            #any people you fight here, the only counters they use are spells
            #place where you maybe can get Wand of Wonder, or Wand of the Chosen using a random integer with a tiny chance of landing on a specific number
        #Whitrock (town of nerds)
            #intelligence reduced by 25-35%
            #slight chance of getting mind control, which is in the secret category
            #fairly good weapons here, but some are specially crafted to have enhanced damage
            #list for weapons
        #Frostpeaks (mountainous and cold area)
            #this is the hardest place to go to behind the capital
            #strength and dexterity reduced by 25-50%
            #very high mountains have to be climbed, but you get the most insane loot from this area
            #enemies placed randomly around the map, their only weakness is fire
            #can tame a bear for temporary increase in speed
            #but it is possible that the bear will attack you if a random integer doesn't meet a conditional's requirements
            #a list of super weapons you can get here
        #Drappes (capital)
            #you have to fight just to even get into the town
            #impossible to go into this town immediately at the beginning of the game, most likely won't even be an option until at least 3 towns have been gone through
            #guards around every corner, you barely will make it around the tall buildings without getting caught
            #Dragon King is waiting in the tallest building in the city
            #absolutely insane loot here, but incredibly hard to get, risky business
            #a list for the loot
"""-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
#Boss function
    #damage will be 75% more than everything else
    #this will be the only combat where the opponent will use both spells AND weapons
    #weapons that the boss has will be randomly chosen from a list
    #if you die here, no checkpoint. You get sent all the way back to the beginning of the game. If you didn't come prepared, get cooked.
"""-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
#How it ends after you go through all of the towns:
    #you fight the boss at the end of the game, in the capital
    #the edited and more buffed combat function for the boss gets executed
    #if you lose against the boss, you get sent all the way back to the beginning of the game most likely through the re-execution of a city function or the while loop that the whole code is in
    #while loop will be while dead is false
    #if dead equals to true, you go to the beginning of the current town that you are in
    #once you beat the boss, there is a massive dialogue
    #then after that, there is an input that asks if you want to play the game again, then it re-executes the entire while loop from the beginning