#EHCP2

"""with open("EH_CP1/notes/notes_files.txt", "w") as file:
    file.write("Bruh1\n")
    file.write("Bruh2\n")
    file.write("Bruh3")"""
'''content = []
with open("EH_CP1/notes/notes_files.txt") as file:
    for line in file:
        content.append(line)

    index = content.index("Bruh\n")
    content[index] = "Huh"
    file.truncate(0)

    for name in content:
        file.write(name = "\n")'''

import csv
"""with open("EH_CP1/notes/sample.csv", "w", newline = '') as csvfile:
    names = ['username', 'favorite color']
    writer = csv.writer(csvfile)

    writer.writerow(names)
    writer.writerow(["cosmic_voyager", "indigo"])
    writer.writerow(["wizard", "bruh"])"""
users = [["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],["cosmic_voyager", "indigo"],]

with open("EH_CP1/notes/sample.csv", "a", newline = '') as csvfile:
    names = ['username', 'favorite color']
    writer = csv.writer(csvfile)

    writer.writerow(users)