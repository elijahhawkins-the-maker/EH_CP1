#EHCP2
import math as m
print("Welcome to the financial calculator!")
try:
    usr = int(input("What would you like to do in this calculator?\n1 for Savings time calculator\n2 for Compound Interest Calculator\n3 for Budget Allocator\n4 for Sale Price Calculator\n5 for Tip Calculator"))
except ValueError:
    print("This ain't something you can do!")

def tip():
    tipp = int(input("What is the percentage that you would like to tip?\n"))
    total = float(input("What is the total of what you are buying?\n"))

    
    tipp /= 100 + 1
    total *= tipp
    print(f"Your new total is going to be ${tipp}")
if usr == 5:
    tip()