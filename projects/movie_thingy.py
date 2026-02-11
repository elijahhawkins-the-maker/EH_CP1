#EHCP1
import csv

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
        usr = input("What is the movie that you would like to find?\nSearch anything\n").capitalize()
        found_movies = [x for x in content if any(usr in str(v) for v in x.values())]

        if found_movies:
            for movie in found_movies:
                title = movie.get('Title', "N/A")

        else:
            print(f"No matches found")
find_movie()