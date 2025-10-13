#EH 1st password strength checker
p_characters = ["!","@","#","$","%","^","*","(",")","[","]",",",".","<",">","/","'","|",":",";","_","'"]
# declare a list with all of the special characters in it
while True:
# make a while loop that re-plays the code
    p = input("what is your password that you want to check the strength of?\n")
#ask user for the password through an input
    if p in p_characters:
