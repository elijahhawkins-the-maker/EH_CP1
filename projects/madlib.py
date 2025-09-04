#EH_madlib 1st
print("Try to make a funny story by entering in some words!")

Name = input("Enter your name (or a random name , ex: ryan reynolds):\n     ")
place = input("Enter a random place (like the mall or walmart):\n    ")
isle = input("enter in a section in the place (like a chips section or something):\n   ")
item = input("Enter a random item:\n     ")
verb = input("enter a random verb (such as 'walk' but more funny):\n   ")
item2 = input("enter a second item from that section:\n     ")
car = input("enter a car:\n    ")
incident = input("enter an incident (their car crashed! or something):\n  ")
car2 = input("enter in a second different car:\n    ")

story = (" once upon a time, a guy or gal named " + (Name) + " decided to " + (verb)
+ " to " + (place) + " to get " + (item) + " but once they went into the " + (place)
+ "," + " they remembered that they needed to also get, " + (item2) + "!" + " so they " + (verb)
+ " over to the " + (isle) + " to get " + (item2) + "." + " After they got " + (item2)
+ "," + " they went to the cash register to check out." + " After they checked out, " + (Name)
+ " went to their " + (car) + " and began to drive away! But just before they thought they were home free, they ran into a problem. "
+ (incident) + "," + " So he wasn't able to get home! But in the end, he managed to get home anyways, because he bought a new "
+ (car2) + "! So in the end, he not only got home, got his stuff from " + (place) + "," " but he got a new car too!")

print(story)