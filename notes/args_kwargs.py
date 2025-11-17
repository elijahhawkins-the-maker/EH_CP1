#EH 1st args kwargs

"""def hello(name = "urmom", age = 21):
    return f"hello {name}!"

print(hello())
print(hello("Bruh2", 21))
print(hello("bruh3"))
print(hello(age = 27))"""

def hello(*names, **bruh):
    print(type(names))
    print(bruh)
    for n in names:
        print(f"hello {n} {bruh['last_name']}" )

hello("alex", "bruh", "nah", "jit", "trippin", last_name = "Hawkins")

def full(**names):
    if 'middle' in names.keys():
        return f"{names['first']} {names['last']}"
    else:
        return f"{names['first']}, {names['last']}"
print(full(first="koro", last="sensei"))
print(full(first="sigma", middle="sigma", last="boy"))

def summary(**story):
    sum = ""
    if "name" in story.keys():
        sum+= f"{story['name']} is the main character of this story."
    if "place" in story.keys():
        sum += f"the story takes place in {story['place']}."
    if "conflict" in story.keys():
        sum+= f"the problem is {story['conflict']}."
    return sum
print(summary(name = "luke skyrunner", place = "a galaxy far far away"))