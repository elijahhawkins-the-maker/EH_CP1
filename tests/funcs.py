#Helper Functions
import sys as s
import time as t

def typing(text, delay=0.03):
    for char in text:
        s.stdout.write(char)
        s.stdout.flush()
        t.sleep(delay)

