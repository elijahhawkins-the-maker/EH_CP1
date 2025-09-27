#EH 1st rock paper scissors
import random

rps = ["rock", "paper", "scissors"]

print(" I challenge you to rock paper scissors! choose your attack!")

user = input("type your attack below:\n ")


if user in rps:
    rand_choice = random.choice(rps)
    if rand_choice == "rock" and user == "rock":
        print(f"You picked {user} and your opponent picked {rand_choice} you tie!")
    elif rand_choice == "rock" and user == "paper":
        print(f"You picked {user} and your opponent picked {rand_choice} you won!")
    elif rand_choice == "rock" and user == "scissors":
        print(f"You picked {user} and your opponent picked {rand_choice} you lost!")
    elif rand_choice == "paper" and user == "rock":
        print(f"You picked {user} and your opponent picked {rand_choice} you lost!")
    elif rand_choice == "paper" and user == "paper":
        print(f"You picked {user} and your opponent picked {rand_choice} you tie!")
    elif rand_choice == "paper" and user == "scissors":
        print(f"You picked {user} and your opponent picked {rand_choice} you won!")
    elif rand_choice == "scissors" and user == "rock":
        print(f"You picked {user} and your opponent picked {rand_choice} you won!")
    elif rand_choice == "scissors" and user == "paper":
        print(f"You picked {user} and your opponent picked {rand_choice} you lost!")
    elif rand_choice == "scissors" and user == "scissors":
        print(f"You picked {user} and your opponent picked {rand_choice} you tie!")
else:
    print("invalid input my guy!")

