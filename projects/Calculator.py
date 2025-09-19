#EH period 1 basic calculator
print("Yo here is a fully functioning calculator!!!")

e = input("What equation would you like the calculator to solve?\n add for addtion\n sub for subtraction\n m for multiplication\n d for division\n mod for modulo\n int for integer division\n ex for exponents\n ")
if e == ("add"):
    add = float(input("alrighty then what is the first number:\n     "))
    add2 = float(input("alrighty now what is the second number:\n    "))
    add3 = float(add + add2)
    add4 = round(add3, 2)
    print(add, "+", add2, "=", add4)
elif e == ("sub"):
    sub = float(input("alrighty what is the first number:\n    "))
    sub2 = float(input("alrighty now what is the second number:\n   "))
    sub3 = float(sub - sub2)
    sub4 = round(sub3, 2)
    print(sub, "-", sub2, "=", sub4)
elif e == ("m"):
    mul = float(input("alrighty what is the first number:\n    "))
    mul2 = float(input("alrighty what is the second number:\n    "))
    mul3 = float(mul * mul2)
    mul4 = round(mul3, 2)
    print(mul, "*", mul2, "=", mul4)
elif e == ("d"):
    div = float(input("alrighty what is the first number:\n    "))
    div2 = float(input("alrighty what is the second number:\n    "))
    div3 = float(div / div2)
    div4 = round(div3, 2)
    print(div, "/", div2, "=", div4)
elif e == ("mod"):
    mod = float(input("alrighty what is the first number:\n    "))
    mod2 = float(input("alrighty what is the second number:\n    "))
    mod3 = float(mod % mod2)
    mod4 = float(mod3, 2)
    print(mod, "%", mod2, "=", mod4)
elif e == ("int"):
    int = float(input("alrighty what is the first number:\n    "))
    int2 = float(input("alrighty what is the second number:\n    "))
    int3 = float(int // int2)
    int4 = round(int3, 2)
    print(int, "//", int2, "=", int4)
elif e == ("ex"):
    ex = float(input("alrighty what is the first number:\n    "))
    ex2 = float(input("alrighty what is the second number:\n    "))
    ex3 = float(ex ** ex2)
    ex4 = round(ex3, 2)
    print(ex, "**", ex2, "=", ex4)
else: 
    print("not a valid operator, bruh")
