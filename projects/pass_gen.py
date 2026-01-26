#EHCP2
import random as r
import string

for x in range(6):
    print(r.choice(string.ascii_lowercase))
    print(r.choice(string.ascii_uppercase))
    print(r.randint(1,9))