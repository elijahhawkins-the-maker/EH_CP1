# EH 1st formatting outputs

# how do i write a format method?
name = "bruh"
age = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
money = 67676767676767676767676767.67
percent = .67
print("hello {}, you are {:e}. That is so old!. you have ${:.2f}, you must be rich! random percent: {:%}".format(name,age,money,percent))

#:b puts it in binary mode
#:e puts it into to scientific notation
#:% turns into a percent
#:, puts comma between numbers
print(f"hello {name}, you are {age:,}. you are fudging old! you have {money:.2f}, you must be rich! random percent is {67/100:%}.")
