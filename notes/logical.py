#EH 1st logical operators

grade = 100

if grade > 100:
    print(f"you got extra credit ... you did {grade - 100}% extra credit")
elif grade == 100:
    print("your grade is perfect")
else:
    print(f"try harder or else you are a massive skill issue, your grade is only {grade}. ")

username = "elijah"
password = "password123"

user = input("what is your username: ")
pw = input("enter your password:  ")
if not user or not pw:
    print("please enter valid input")
elif user == "bruh" and pw == "password":
    pass
elif user == username and pw == password:
    print("welcome elijah")
elif user == username:
    print("password is incorrect")
else:
    print("incorrect credentials")