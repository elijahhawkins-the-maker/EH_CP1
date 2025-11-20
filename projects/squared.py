#EHCP1 squared numbers
#import math at the top
import math
#set an empty list for the numbers entered
nums = []
#while loop with a try and except statement inside of it that checks if numbers are continuously being entered in it
while True:
    try:
        usr = float(input("What are the numbers that you would like to find the square of?\nEnter anything that isn't a number to stop\n"))
        #adds the numbers entered to the list
        nums.append(usr)
        #if ValueError occurs, it breaks the loop
    except ValueError:
        print("Ending entering of numbers")
        break
#this function squares the numbers
new_nums = map(lambda num: num**2 ,nums)
#this prints the squared numbers out until it reaches the end of the list
for num in new_nums:
    print(f"original number: {int(math.sqrt(num))} squared number: {num}")