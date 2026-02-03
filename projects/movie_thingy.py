#EHCP1
import csv
import re
try:
    with open("EH_CP1\projects\Movies list - Sheet1.csv") as movies:
        read = csv.reader(movies)
        header = next(read)
        content = []
        for x in read:
            content.append(
                {
                    header[0]: x[0],
                    header[1]: x[1],
                    header[2]: x[2],
                    header[3]: x[3],
                    header[4]: x[4]
                }
            )
except:
    print("can't find file")
else:
    for movie in content:
        print(movie)

def find_movie():
    choice = input("How would you like to find a movie?\nYou can find it by director,\nMovie name\na single letter maybe\nWhatever you want to search it by\n")
    for x in content:
        bruh = re.search(content, choice)
        print(x)
    print("These are your matches")
find_movie()