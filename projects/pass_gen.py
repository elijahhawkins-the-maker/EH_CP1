#EHCP2
import random as r
import string
#string library converts any data set to a string automatically
import time as t
def main():
    #welcomes user to the password generator
    print("Welcome to the Random Password Generator!")
    #while loop so that the user HAS to input the correct thing
    while True:
        try:
            user = int(input("What would you like to do?\n 1 for generating a few passwords\n 2 for exiting the platform\n"))
            if user == 1:
                pass_input()
            elif user == 2:
                return
        except ValueError:
            print("That ain't something you can do!")
            
def pass_input():
    #inputs for the password generation (some passwords generated may not have all types of characters, but others will)
    while True:
        try:
            gens = int(input("How many passwords would you like to generate?\n"))
            length = int(input("What is the length of the password you would like to create?\n"))
            break
        except ValueError:
            print("You can't do that!")
    nums = input("Would you like numbers in your password?\ny or n\n")
    spec_char = input("Would you like special characters in your password?\ny or n\n")
    cap_letters = input("Would you like capital letters in your password?\ny or n\n")
    low_letters = input("Would you like lowercase letters in your password?\ny or n\n")

    def pass_gen():
        data = ""
#if statements to check whether user types yes or no
        if nums == "y":
            data += string.digits
        if spec_char == "y":
            data += string.punctuation
        #use ascii and string library because it is superior and you don't have to use a massive list
        if cap_letters == "y":
            data += string.ascii_uppercase
        if low_letters == "y":
            data += string.ascii_lowercase
        #for loop that generates user input number of passwords
        number = 1
        for i in range(gens):
            pas = ''.join(r.choice(data) for x in range(length))
            print(f"#{number} is {pas}")
            number += 1
    #if statement to actually generate password if any equal yes
    if nums == "y" or spec_char == "y" or cap_letters == "y" or low_letters == "y":
        pass_gen()
    #this executes only if none are yes
    else:
        print("You gotta have somethin in your password!")
        t.sleep(2)
main()