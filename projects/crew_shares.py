#EH 1st crew shares
money = int(input("how much money did your crew make:\n   ").strip().strip("$"))
crew = int(input("how many crew members are there:\n   ").strip())
share = money / (crew + 10)
captain = share * 7
first = share * 3
print(f"the captain gets this much money: ${captain:.2f}\nthe first mate gets this much money: ${first:.2f}\nthis is how much money each crew member gets {(share - 500):.2f}")