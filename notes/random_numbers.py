#EH 1st random numbers
import random

name = input("what is your character name\n").strip()

stat_one = random.randint(1,10) + random.randint(1,10)
stat_two = random.randint(1,10) + random.randint(1,10)
stat_three = random.randint(1,10) + random.randint(1,10)
stat_four = random.randint(1,10) + random.randint(1,10)
stat_five = random.randint(1,10) + random.randint(1,10)
stat_six = random.randint(1,10) + random.randint(1,10)
stat_seven = random.randint(1,10) + random.randint(1,10)

print(f"your stat options are: {stat_one}, {stat_two}, {stat_three}, {stat_four}, {stat_five}, {stat_six}, {stat_seven}")

#set stats
strength = int(input("which stat do you want as your strength: \n")) +2

print(f"this is a random number between 0 and 1: {random.random()}")
print(f"this is a random number from 1 to a trillion or more: {random.randint(1,9999999999999999999999999999999999999999999999999999999999999)}")
