#EH 1st rock paper scissors
import random

s = {
    "user":0,
    "computer":0
}

while True:
    rps = ["rock", "paper", "scissors"]

    print(" I challenge you to rock paper scissors! choose your attack!")
    print("or just type in stop to stop the match!")

    user = input("type your attack below:\n ")

    if user in rps:
        rand_choice = random.choice(rps)
        if rand_choice == "rock" and user == "rock":
            print(f"You picked {user} and your opponent picked {rand_choice} you tie!")
        elif rand_choice == "rock" and user == "paper":
            print(f"You picked {user} and your opponent picked {rand_choice} you won!")
            s["user"] += 1
        elif rand_choice == "rock" and user == "scissors":
            print(f"You picked {user} and your opponent picked {rand_choice} you lost!")
            s["computer"] += 1
        elif rand_choice == "paper" and user == "rock":
            print(f"You picked {user} and your opponent picked {rand_choice} you lost!")
            s["computer"] += 1
        elif rand_choice == "paper" and user == "paper":
            print(f"You picked {user} and your opponent picked {rand_choice} you tie!")
        elif rand_choice == "paper" and user == "scissors":
            print(f"You picked {user} and your opponent picked {rand_choice} you won!")
            s["user"] += 1
        elif rand_choice == "scissors" and user == "rock":
            print(f"You picked {user} and your opponent picked {rand_choice} you won!")
            s["user"] += 1
        elif rand_choice == "scissors" and user == "paper":
            print(f"You picked {user} and your opponent picked {rand_choice} you lost!")
            s["computer"] += 1
        elif rand_choice == "scissors" and user == "scissors":
            print(f"You picked {user} and your opponent picked {rand_choice} you tie!")
    elif user == "stop": 
        print("alrighty exiting the program")
        break
    else:
        print("invalid input my guy!")
    print(f"your score is {s["user"]} and your opponents score is {s["computer"]}")
    continue

