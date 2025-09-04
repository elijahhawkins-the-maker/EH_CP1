#EH 1st string method notes

subject = "computer programming 1!"

print(subject.upper()) #all letters capitalized
print(subject.lower()) #all letters lowercase
print(subject.center(100))

# stupid idiot proofing
color = input("what is your favorite color?")
print("that is cool. i like" + color + "too!")

#idiot proofing inputs
color = input("what is your favorite color?").strip().capitalize()
# lower() is all lower case
# upper() is all upper case
# title() capitilizes first letter of every word
# capitilize() capitilizes first letter
full_name = input("what is your full name").strip().title()
#print("that is cool {full_name}. I like {color} too")

# f strings
print(f"that is cool {full_name}. i like {color} too!")
pi = 3.141592653589793238634626

#print(f."we all know pi is equal to {pi:.3f}")
#print(pi.isdecimal())

sentence = "the quick brown fox jumped over the lazy dog"
word = "jumps"
print(sentence.find(word))
start = sentence.index(word)
length = len("lazy")
print(sentence[start:start+length])
print(sentence.replace(word, "swims"))
print(sentence)
