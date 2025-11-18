#EHCP1 flex calc
while True:
    try:
        user = int(input("What is the operation that you would like to do on the flexible calculator? There is...\n 1 for Finding the min of some numbers\n 2 for Finding the max of some numbers\n 3 for Finding the product of some numbers\n 4 for Finding the average of some numbers \n 5 for Find the sum of some numbers\n"))
    except ValueError:
        print("You must enter in a number")
    def mini():
        global numbers
        numbers = []
        while True:
            try:
                user = float(input(f"What is the numbers that you would like to find the mininum of?\n and if you are done type anything that isn't a number"))
                numbers.append(user)
            except ValueError:
                print("You have chosen to end entering numbers")
                break
        for num in numbers:
            print(numbers)
        minimum = min(numbers)
        print(f"the minimum of {numbers} is {minimum}")
    if user == 1:
        mini()
    else:
        print("bruh")