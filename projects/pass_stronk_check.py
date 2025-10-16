#EH 1st password strength checker
#print statement to welcome the user
import re
#import re into the program to search for the characters (yay new cool library found)
print("Welcome to the password strength checker!")
#add this index to the program that has all special characters in it
p_characters = r"[^a-zA-Z0-9\s]"
#add this index aswell that has all uppercase letters in it (yes the other one has uppercase but I wanted to use this one)
uppercase = r"[A-Z]"
#make a while loop that replays the code
while True:
#thing that keeps track of the score
    score = 0
#asks user for the password
    pas = input("What is your password that you would like to check? Enter below.\n")
#each if statement adds 1 to the score if the password is good
#if statement that will see if the length is over 8 characters
    if len(pas) >= 8 - 1:
        print("You have successfully added more than 8 characters to your password!")
        score += 1
    else:
        print("Your password needs to be 8 characters or more")
#have a break function at the end of every for loop or else the loop will continue forever
#but for the while loop, have no break function because we want the loop to continue
#if statement using the re.search function that checks a p_characters for special characters in the password
    if re.search(p_characters, pas):
        print("You have successfully put a special character in your password")
        score += 1
    #else statement that will happen if it isn't 8 characters or more
    else:
        print("You need to put a special character in your password")
    #if statement that will check if there is a number in the password
    if any(char.isdigit() for char in pas):
        print("You've successfully added one number")
        score += 1
    #else statement that will execute only if the if statement isn't true
    else:
        print("You need to put a number into the password")
    #for loop with an if statement in it that checks the password if it has lowercase letters         
    for c in pas:
        #another for loop with an if statement that checks if the password has any lowercase letters
        if c.islower:
            print("You've successfully added one or more lowercase letters")
            score += 1
            break
        #else statement that is after the if statement that will exeucute only if the if statement isn't true
        else:
            print("You need to put a lowercase letter into your password")
            break
    #if statement that checks if the password has uppercase letters using the re.search function that checks all characters of the input string
    if re.search(uppercase, pas):
        print("You've successfully added one or more uppercase letters")
        score += 1
        #else statement that will execute only if the if statement isn't true
    else:
        print("You need to add an uppercase letter to your password")
    #print statement that tells the user their score
    print(f"Your score after your password evaluation is {score} point(s)!")

    #if statements that tell the evaluation of the password based on the score
    if score <= 2:
        print("Your password is weak")
    elif score == 3:
        print("Your password is not too bad, but it aint that good")
    elif score == 4:
        print("Your password is strong")
    elif score == 5:
        print("Your password is excellent!")