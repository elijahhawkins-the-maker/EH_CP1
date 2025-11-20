#EHCP1 flex calc
#import math and statistics to find the average and products
import statistics as s
import math as m
#while loop that runs the code continuously
while True:
    #try and except statement that checks whether a number has been entered or not
    try:
        user = int(input("What is the operation that you would like to do on the flexible calculator? There is...\n 1 for Finding the min of some numbers\n 2 for Finding the max of some numbers\n 3 for Finding the sum of some numbers\n 4 for Finding the average of some numbers \n 5 for Finding the product of some numbers\n"))
    except ValueError:
        print("You must enter in a number")
    #make a function that checks what the minimum of numbers in a list is
    def mini(*numbers):
        #converts the tuple to a list
        numbers2 = list(numbers)
        #while loop for the numbers to be continuously entered until the try and except statement sees that a number hasn't been entered
        while True:
            try:
                user = float(input(f"What is the numbers that you would like to find the mininum of?\n and if you are done type anything that isn't a number\n"))
                numbers2.append(user)
            except ValueError:
                print("You have chosen to end entering numbers")
                break
        #function that checks the minimum of the list
        minimum = min(numbers2)
        #print statement that shows the user the correct answer
        print(f"the minimum of {numbers2} is {minimum}")
    #if statement that checks whether to execute the function
    if user == 1:
        mini()
    #all other functions are the same but with different calculations and variables and function names
    def maxi(*numbers):
        number2 = list(numbers)
        while True:
            try:
                user = float(input("What are the numbers that you would like to find the max of?\n Enter in anything that isn't a number to stop\n"))
                number2.append(user)
            except ValueError:
                print("You have chosen to stop entering numbers")
                break
        maximum = max(number2)
        print(f"the maximum number of {number2} is {maximum}")
    if user == 2:
        maxi()
    def summ(*numbers):
        numbers2 = list(numbers)
        while True:
            try:
                user = float(input("What numbers would you like to find the sum of?\n Enter in anything that isn't a number to stop\n"))
                numbers2.append(user)
            except ValueError:
                print("You have stopped entering numbers")
                break
        sums = sum(numbers2)
        print(f"The sum of {numbers2} is {sums}")
    if user == 3:
        summ()
    def aver(*numbers):
        numbers2 = list(numbers)
        while True:
            try:
                user = float(input("What numbers would you like to find the average of?\n Enter anything that isn't a number to stop\n"))
                numbers2.append(user)
            except ValueError:
                print('You have stopped entering numbers')
                break
        average = s.mean(numbers2)
        print(f"The average of {numbers2} is {average}")
    if user == 4:
        aver()
    def pro(*numbers):
        numbers2 = list(numbers)
        while True:
            try:
                user = float(input("What numbers would you like to find the product of?\n Enter anything that isn't a number to stop\n"))
                numbers2.append(user)
            except ValueError:
                print("You have stopped entering numbers")
                break
        product = m.prod(numbers2)
        print(f"The product of {numbers2} is {product}")
    if user == 5:
        pro()
        