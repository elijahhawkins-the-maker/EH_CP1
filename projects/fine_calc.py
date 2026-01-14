#EHCP2
def main():
    print("Welcome to the financial calculator!")
    try:
        usr = int(input("What would you like to do in this calculator?\n1 for Savings time calculator\n2 for Compound Interest Calculator\n3 for Budget Allocator\n4 for Sale Price Calculator\n5 for Tip Calculator\n"))
    except ValueError:
        print("This ain't something you can do!")
    #function for the savings time
    def sime():
        #there are print statements to welcome the user and give a brief explanation for each function
        print("This calculator shows the time that it will take to save from $0 to a specified amount")
        #there are usually 2 or more inputs for amounts in functions
        while True:
            save = float(input("What is the amount that you would like to save to?\n"))
            cont = float(input("What is the amount that you are contributing?\n"))
            time = input("How often will you contribute?\nWeekly\nOr monthly?\n")
            #some nice idiot proofing done here
            if time != "monthly" and time != "weekly":
                print("Not a valid time unit!")
            else: 
                break
        #variables needed for controlling loop time
        bruh = 0
        timer = 0
        while True:
            bruh += cont
            timer += 1
            if bruh >= save:
                #checks whether user picked monthly or weekly
                if time == "monthly":
                    print(f"It will take you {timer} months to save ${save}")
                    break
                if time == "weekly":
                    print(f"It will take you {timer} weeks to save ${save}")
    #function for the copmound savings
    def comp():
        print("This shows the money that you will gain over the course of a specified time\n with a certain amount of money\n with an interest rate")
        start = float(input("What is the starting amount in your account?\n"))
        interest = float(input("What is the interest or APR?\n"))
        at = int(input("What is the amount of time you will be saving in years?\n"))
        p = (interest / 100) + 1
        #special formula for compound savings
        new_am = start * (p**at)
        print(f"The amount of money after {at} years will be ${new_am:.2f}")
    #this is the function for budget allocation
    def allocate():
        print("This allows for you to see what you can spend money on during the month with your income!")
        inc = float(input("What is your monthly income/budget?\n"))
        factions = int(input("How many catagories do you want to split your budget into?"))
        factions2 = factions
        percent_left = 100
        summ = []
        while factions > 0:
            percent = int(input(f"What is the percentage of this catagory?\nIt will ask this {factions} times.\nYou have {percent_left} percent to use."))
            #percent_left shows the user how much they can use before they go over 100
            percent_left -= percent
            summ.append(percent)
            total = sum(summ)
            factions -= 1
            if total > 100:
                print("You need to recalculate percentage! It is over 100!")
                percent_left = 100
                factions += factions2
                summ = []
                continue
            if total == 100 and factions == 0:
                print("You calculated the percentage right!")
                break
            if total < 100 and factions == 0:
                print("You need to recalculate percentage! It is too low to be 100!")
                percent_left = 100
                factions += factions2
                summ = []
                continue
        catagory = 1
        for x in summ:
            x /= 100
            new_x = inc * x
            print(f"catagory {catagory} budget is {new_x:.2f}")
            catagory += 1
    #This is the function for discounts
    def s_price():
        print("This shows what a discount can take off of an original price!")
        og = float(input("What is the original price of the item?\n"))
        percent = int(input("What is the discount percentage?\n"))
        
        percent2 = (percent / 100)
        t = percent2 * og
        total_price = og - t
        print(f"The new price after the discount is ${total_price:.2f}")
    #lastly, this is the function for a tip!
    def tip():
        print("This shows the percentage of your bill, converted to a tip amount!")
        tipp = int(input("What is the percentage that you would like to tip?\n"))
        subtotal = float(input("What is the total of what you are buying?\n"))

        tippy = subtotal * (tipp / 100)
        total = subtotal + tippy
        print(f"Your new total is going to be ${total:.2f}\nThe tip is ${tippy:.2f}")
    if usr == 5:
        tip()
    elif usr == 4:
        s_price()
    elif usr == 3:
        allocate()
    elif usr == 2:
        comp()
    elif usr == 1:
        sime()
while True:
    user = input("Would you like to use the functional calculator?\ny or n\n")
    if user == "y":
        main()
        break
    if user == "n":
        print("alrighty")
        break
    else:
        print("You can't do that!")
        