#EH 1st dictionaries

#key: value pairs

pluh = {
    #key:value,
    "name": "Xavier",
    "age": 22,
    "job": "maverik",
    "sibling": ["bruh", "bruh2", "bruh3", "bruh4"]
}

print(pluh["name"])
print(pluh.keys())
for key in pluh.keys():
    if key == "sibling":
        for name in key:
            print(f"{pluh['name']} has a sibling named {name}")
    else:
        print(f"{key} is {pluh[key]}")

