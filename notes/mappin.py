#EH 1st mapping

numbers = [8937285,65387,438754,32654,3467498,873509504626,4]
new_nums = []

"""for number in numbers:
    new_nums.append(number/3)
print(new_nums)"""
def divide(num):
    return num/3

new_nums = map(lambda num: num/3, numbers)
print(list(new_nums))
for num in new_nums:
    print(num)