#EHCP2
#import csv at the top
import csv
#print statement to welcome the user
print("Welcome to the movie recommender")
#function for finding the movie
def find_movie():
    try:
        with open("EH_CP1/projects/Movies list - Sheet1.csv", "r") as movies:
            read = csv.reader(movies)
            header = next(read)
            content = []
            for x in read:
                content.append(
                    {
                        header[i]: x[i] for i in range(len(header))
                    }
                )
    except:
        print("can't find file")
    else:
        pass
    while True:
        try:
            usr = int(input("What would you like to do?\n1 for searching for movies\n2 for diplaying the whole list of movies\n3 for exiting\n"))
            if usr == 1:
                pass
            if usr == 2:
                for i2 in content:
                    for i3 in i2.values():
                        print(i3, ", ")
            if usr == 3:
                print("exiting...")
                return
        except ValueError:
            print("That ain't something you can do!")
        usr2 = input("What is the movie that you would like to find?\nSearch anything\n").capitalize()
        found_movies = [x for x in content if any(usr2 in str(v) for v in x.values())]

        if found_movies:
            for m in found_movies:
                for i in m.values():
                    print(i)

        else:
            print(f"No matches found")
find_movie()