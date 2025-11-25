import sys
import time as clock

nums = 2

sys.set_int_max_str_digits(100000)

while True:

    nums *= 2

    print(f"\033[92m{nums}\033[0m")

    clock.sleep(0.006)