#EH 1st multiplication table
num1 = int(input("what is the first number in the multiplication table\n"))
num2 = int(input("what is the last number in the multiplication table\n"))
for i in range(num1,num2+1):
    print([i*i2 for i2 in range(num1,num2+1)])