#EHCP2
#import time for time between print statements
import time as t
#tuple of letters
letters = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
#tuple of morse code!
morse = (".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--..")

def text_to_morse():
    text_input = input("What is the text that you want to convert to morse code?\n")
    #converts all characters to uppercase so that it can be detected in the index
    text = text_input.upper()
    #string that the morse gets put into for printing
    morse_shown = ""
    #for loop that prints each morse letter that coresponds to the letters in the input
    for i in text:
        if i in letters:
            index = letters.index(i)
            morse_shown += morse[index] + "/"
        #fills in string with nothing so that it doesn't throw an error
        else:
            morse_shown += " "
    print(morse_shown)
    t.sleep(1.5)

#the other function is basically the exact same as the first one but converting morse code to english

def morse_to_text():
    morse_input = input("What is the morse code that you want to convert to text?\nMake sure to separate each morse letter with a space\n")
    #splits each character so that the for loop sees each individual one
    morse_code = morse_input.split(" ")
    text_shown = ""
    for x in morse_code:
        if x in morse:
            index = morse.index(x)
            text_shown += letters[index]
        else:
            text_shown += " "
    print(text_shown.lower())
    t.sleep(1.5)

def main_menu():
    print("Welcome to the morse code translator!\nHere you can see what english is in morse code, and vice versa!")
    #while loop that helps to idiot proof
    while True:
        #try and except for entering integers
        try:
        # if statements that take you to the functions
            choice = int(input("What do you want to do?\n1 for converting text to morse\n2 for converting morse to text\n3 for exiting the program\n"))
            if choice == 1:
                print("Alrighty, you chose to convert text to morse")
                text_to_morse()
            elif choice == 2:
                print("Alrighty, you chose to convert morse to text")
                morse_to_text()
            elif choice == 3:
                print("Alrighty, you chose to exit the program")
                return
            else:
                print("You somehow broke the code! Nah just kidding")
        except ValueError:
            print("That ain't something you can do!")
main_menu()