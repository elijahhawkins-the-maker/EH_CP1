#EH 1st password strength checker
#print statement to welcome the user
print("Welcome to the password strength checker!")
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
#if statement that checks if the user has special characters that is in a for loop with the special characters
#have a break function at the end of every for loop or else the loop will continue forever
#but for the while loop, have no break function because we want the loop to continue
    for c in "!@#$%^*()[],'\.<>/|:;_+=-":
        if c in pas:
            print("You have successfully put a special character in your password")
            score += 1
            break
        #else statement that will happen if it isn't 8 characters or more
        else:
            print("You need to put a special character in your password")
            break
    #if statement that will check if there is a number in the password
    if any(char.isdigit() for char in pas):
        print("You've successfully added one number")
        score += 1
    #else statement that will execute only if the if statement isn't true
    else:
        print("You need to put a number into the password")
    #for loop with an if statement in it that checks the password if it has uppercase letters
    for s in pas.upper():
        if s in pas:
            print("You've successfully added one or more uppercase letters")
            score += 1
            break
        #else statement that will execute only if the if statement isn't true
        else:
            print("You need to add an uppercase letter to your password")
            break
    for x in pas:
        #another for loop with an if statement that checks if the password has any lowercase letters
        if any(x.lower()):
            print("You've successfully added one or more lowercase letters")
            score += 1
            break
        #else statement that is after the if statement that will exeucute only if the if statement isn't true
        else:
            print("You need to put a lowercase letter into your password")
            break
    #print statement that tells the user their score
    print(f"Your score after your password evaluation is {score} point(s)!")


    