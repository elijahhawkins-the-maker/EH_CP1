#EH 1st idiot proof
gpa = float(input("What is your gpa?   "))
fname = input("what is your first name?    ")
lname = input("what is your last name?    ")
fphone = input("enter the first three digits of your phone number: ")
sphone = input("enter the second three digits of your phone number:    ")
tphone = input("enter the last four digits of your phone number:   ")

phone = (fphone + " " + sphone + " " + tphone)
gpa2 = round(gpa, 1)

print(gpa2)
name = (fname + " " + lname)
name2 = name.title()
print(name2)
print(phone)