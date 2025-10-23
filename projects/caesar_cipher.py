#EH 1st caesar cipher
#while loop that runs the code continuously
while True:
    #print statement to welcome the user
    print("Welcome to the caesar cipher! where you get your encoded and decoded message!")
#first function that encodes the entered message
    def encode(text, shift):
        #the etext is so you're able to return the decoded or encoded text to the user
        etext = ""
        #for loop that checks for uppercase and lowercase letters in the input
        for char in text:
            #if statement for lowercase
            if 'a' <= char <= 'z':
                s = ord('a')
            #second if statement for uppercase
            elif 'A' <= char <= 'Z':
                s = ord('A')
                #else statement that adds the characters to the etext temporarily aswell as keeps numbers the same
            else:
                etext += char
            #these 2 lines of code gets rid of the original characters, then adds the newly encoded ones to etext
            sc = (ord(char) - s + shift) % 26 + s
            etext += chr(sc)
            #return statement that shows the user the encoded text
        return etext
    #second function that decodes the text that you enter!
    def decode(text, shift):
        #basically just returns the code that the user entered
        return encode(text, -shift)
    #if statement that checks if the code is ran in the file that it has been made in or not (yay no copy pasting allowed!)
    if __name__ == "__main__":
        #finally the user input that takes in the text to encode/decode
        utext = input("enter the thing that you would like to encode or decode:\n")
        #while loop that has a try statement in it that checks if the user has inputed an integer
        while True:
            try:
                ushift = int(input("What would you like to shift by?\n"))
                #break statement that ends the while loop
                break
            #except statement that displays the print statement to the user only if the string cannot be converted to an int (yay try and except are cool!)
            except ValueError:
                print("must enter number without a decimal and no entering letters")
        #this line of code is using the function "encode" again to print the encoded text to the user
        etext2 = encode(utext, ushift)
        print(f"The newly encoded text is {etext2}")
        #this line of code is using the function "decode" again to print out the decoded text to the user
        dtext = decode(etext2, ushift)
        print(f"the decoded text is {dtext}")