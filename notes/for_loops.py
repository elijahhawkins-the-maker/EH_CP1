#EH 1st for loops

nums = [4,67,41,21,567,654,87,243,75,123,7654,980]

for num in nums:
    num /= 2
    if num > 100:
        print(f"{num} is only half of {num*2} It is a large number")
    else:
        print(num)