#EHCP1 factorial calculator
#import math for the factroial function
import math as m
#import sys so then you set the max terminal digits to a few mil
import sys
sys.set_int_max_str_digits(100000000)
"""__________________________________________________________________"""
#for num in num
#def factorial(num-=1)
#if num == 1
#print(f"{num} is the og, and {fac} is the factorial)
#this is the original pseudocode, but it isn't enough, so here is my version:
"""__________________________________________________________________"""
#print statement that welcomes the user
print("Welcome to the factorial calculator!")
#while loop that runs the code continuously
while True:
    #empty list that the numbers get added to
    numbers = []
    #another while loop that makes the input run again if the input isn't an integer
    while True:
        #try and except statement that runs the code only if the input is an integer
        try:
            usr = int(input("What is the number that you would like to find the factorial of?\n"))
            #adds the user input to the list
            numbers.append(usr)
            #adds a multiplication symbol to the list after the numbers
            numbers.append("*")
            #this function makes the factorial
            bruh = m.factorial(usr)
            #this checks whether the input is 0
            if usr == 0:
                print("0=1")
                break
            break
        except ValueError:
            print("Please enter an integer")
    #for loop that makes the numbers print out nice and fancy and also adds the numbers to the list until 1
    for num in numbers:
        usr -= 1
        numbers.append(usr)
        numbers.append("*")
        #if statement that ends the loop when the input value comes all the way down to 1
        if usr == 1:
            #this removes the last multiplication symbol in the list
            numbers.pop()
            for i in numbers:
                print(f"{i}")
            break
#prints the final answer
    print(f"The factorial is {bruh}")