#EHCP1
import csv
try:
    with open("EH_CP1/notes/notes_files.txt", "r") as file:
        content = []
        for line in file:
            content.append(line.strip())
except:
    print("cant find the file")
else:
    for line in content:
        print(f"hello {line}")

try:
    with open("EH_CP1/notes/sample.csv", mode = "r") as sample:
        reader = csv.reader(sample)
        header = next(reader)
        users = []
        for line in reader:
            users.append(
                {
                    header[0]: line[0],
                    header[1]: line[1]
                }
            )
            
except:
    print("can't print")
else:
    for user in users:
        print(user)