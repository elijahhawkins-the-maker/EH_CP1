#EHCP1 squared numbers
import math
while True:
    try:
        usr = float(input("What are the numbers that you would like to find the square of?\nEnter anything that isn't a number to stop\n"))
    except ValueError:
        print("Ending entering of numbers")
        break
nums = []
nums.append(usr)
new_nums = map(lambda num: num**2 ,nums)
for num in new_nums:
    print(f"original number: {int(math.sqrt(num))} squared number: {num}")