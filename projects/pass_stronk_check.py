#EH 1st password strength checker
#print statement to welcome the user
print("Welcome to the password strength checker!")
p_characters = ["!","@","#","$","%","^","*","(",")","[","]",",",".","<",">","/","'","|",":",";","_","'",'"',"+","=","-","{","}"]
#declare a list with all of the special characters in it
#declare a list with all of the numbers in it
p_numbers = [1,2,3,4,5,6,7,8,9]
#create a score holder that keeps track of the score
score = 0
#make a while loop that replays the code
while True:
#make a list that will save the amount of points that you scored the try before
    pro = []
#add a dictionary that keeps track of the specification of the password
    specs = {
    "password_8+":False,
    "contains_uc":False,
    "contains_lc":False,
    "contains_spec_c":False,
    "contains_num":False
    }
#asks user for the password
    pas = input("What is your password that you would like to check? Enter below.\n")
#if statement that will see if the length is over 12 characters
    if len(pas) < 8:
        
#elif statement that checks if the user has special characters
#elif statement that checks if the user has numbers in their password
#elif statement that checks if the user has an uppercase letter in their password
#elif statement that checks if the user has an lowercase letter in their password
#append function that adds the score of your password to the list