#EH 1st order up!

main = {
    "burger":9.99,
    "nachos":11.99,
    "burrito":6.99,
    "extra_crispy_burrito":19.99,
    "taco_special":15.99,
    "quesadilla":4.99,
    "taco_burger":7.99,
    "gun_shaped_steak":99.99
}

sides = {
    "fries":2.99,
    "extra chips":0.99,
    "small_burrito":1.99,
    "small_soda":0.99,
    "medium_soda":1.99,
    "large_soda":2.99,
    "extra_large_soda":3.99
}
des = {
    "ice cream":3.99,
    "bruh":9.99
}

for key in main.keys():
    if key in main:
        for i in key:
            print(main)