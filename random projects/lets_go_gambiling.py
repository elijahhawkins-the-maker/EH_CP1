#slot machine in the works
import random
import time as clock

attributes = {
    "tokens":10,
    "multiplier":1 
}

slot_thingys = [7, "lemon", "bell", 666, "four leaf clover", "cherry"]

rolls = float(input("how many times do you want to use the slot machine,\n each run costs 1 coin so far\n your limit is 10 times \n"))

while True:
    if rolls == (1-10):
        rand_roll = random.choice(slot_thingys)
        print(f"{rand_roll} {rand_roll} {rand_roll}")
