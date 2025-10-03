# EH 1st while loops
import time as clock
import random
#infinite loop
num = 1

while num <= 20:
    clock.sleep(1)
    print(num)
    num += 1 #prevents an inf loop

goose = random.randint(1,20)
count = 0

while count == goose:
    count += 1
    if count == goose:
        break
    else:
        print("duck")

print("goose")

i = 0

while i < 20:
    if i == 10:
        print("i is 10")
        continue
    else:
        print(f"{i} iteration of the loop")
    i+=1
print("the loop has ended")