#EH 1st password strength checker
#print statement to welcome the user
print("Welcome to the password strength checker!")
p_characters = ["!","@","#","$","%","^","*","(",")","[","]",",",".","<",">","/","'","|",":",";","_","'",'"',"+","=","-","{","}"]
#declare a list with all of the special characters in it
#create a score holder that keeps track of the score
score = 0
#make a while loop that replays the code
while True:
#make a list that will save the amount of points that you scored the try before
    progress = []
#asks user for the password
    pas = input("What is your password that you would like to check? Enter below.\n")
#if statement that will see if the length is over 12 characters
    if len(pas) <= 8:
        print("You need to add more then 8 characters to your password")
#if statement that checks if the user has special characters
    for x in p_characters:
        if x not in pas:
            print("You need to have special characters in your password (!,#,@)")
    if not pas.isnumeric():
        print("You need to put at least one number in your password")
    if not pas.upper():
        print("You need to add at least one uppercase letter")
    if not pas.lower():
        print("You need to add at least one lowercase letter to your password")
#if statement that checks if the user has numbers in their password

#if statement that checks if the user has an uppercase letter in their password
#if statement that checks if the user has an lowercase letter in their password
#append function that adds the score of your password to the list