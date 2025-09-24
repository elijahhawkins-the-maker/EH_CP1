#EH 1st Letter grade

grade = float(input("What is your percentage in your class\n "))

if grade <= 200 and grade >= 92:
    print("Your grade is an A!")
elif grade <= 91.99 and grade >= 90:
    print("Your grade is an A-")
elif grade <= 89.99 and grade >= 87:
    print("Your grade is a B+")
elif grade <= 86.99 and grade >= 82:
    print("Your grade is a B")
elif grade <= 81.99 and grade >= 80:
    print("Your grade is a B-")
elif grade <= 79.99 and grade >= 77:
    print("Your grade is a C+")
elif grade <= 76.99 and grade >= 72:
    print("Your grade is a C")
elif grade <= 71.99 and grade >= 70:
    print("Your grade is a C-")
elif grade <= 69.99 and grade >= 67:
    print("Your grade is a D+")
elif grade <= 66.99 and grade >= 64:
    print("Your grade is a D")
elif grade <= 63.99 and grade >= 55:
    print("Your grade is a D-")
elif grade <= 54.99:
    print("Your grade is a big fat F")
else:
    print("not a valid input")
