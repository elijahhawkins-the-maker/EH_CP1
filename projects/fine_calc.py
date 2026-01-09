#EHCP2
import math as m
print("Welcome to the financial calculator!")
try:
    usr = int(input("What would you like to do in this calculator?\n1 for Savings time calculator\n2 for Compound Interest Calculator\n3 for Budget Allocator\n4 for Sale Price Calculator\n5 for Tip Calculator"))
except ValueError:
    print("This ain't something you can do!")

def save_time():
    time = input("How often are you contributing money to what you're saving?\nweekly\n or monthly\n")
    time2 = float(input(f"What amount are you contributing to the money {time}?\n"))
    goal = float(input("What is the amount of money you are trying to save to?"))


