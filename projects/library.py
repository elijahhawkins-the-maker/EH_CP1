#EHCP2
#importing time for delay between print statements
import time as t
import csv
print("Welcome to YOUR personal library!")
fieldnames = ['title', 'author', 'year', 'genre', 'format', 'rating', 'notes']

def add():
    title = input("What is the title of the book that you want to add?\n")
    author = input("Who is the author of the book?\n")
    year = int(input("What is the year the book was published?\n"))
    genre = input("What is the genre of the book?\n")
    format = input("What is the format\n e.g. poem or normal\n")
    rating = float(input("What is the rating of the book?\n"))
    notes = input("Is there any extra notes you want to add?\n")
    total_inputs = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "format": format,
        "rating": rating,
        "notes": notes
        }
    try:
        with open("projects/lib.csv", "r") as file:
            char = file.read(1)
            header = not char
    except FileNotFoundError:
        header = True

    with open("projects/lib.csv", "a", newline = '') as library:
        writer = csv.DictWriter(library, fieldnames=fieldnames)

        if header:
            writer.writeheader()

        writer.writerow(total_inputs)
    print("Now everything has been added to the library")
    t.sleep(1)
    return main_menu()

def view():
    print("Alrighty here is what you have")
    with open("projects/lib.csv", "r") as library:
        reader = csv.DictReader(library, fieldnames=fieldnames)
        for x in reader:
            print(x)
            t.sleep(1)
        return main_menu()
        
def remove():
    title = input("What is the title of the book that you want to remove?\n")
    with open("projects/lib.csv", "r") as library:
        reader = csv.DictReader(library, fieldnames=fieldnames)
        for row in reader:
            if row["title"] == title:
                print(f"Alrighty, you chose to remove {title}")
                with open("projects/lib.csv", "w", newline = '') as library:
                    writer = csv.DictWriter(library, fieldnames=fieldnames)
                    for row in reader:
                        if row["title"] != title:
                            writer.writerow(row)
                            print(f"You successfully removed {title}")
                            return main_menu()

def update_item():
    title = input("What is the title of the book that you want to update?\n")
    with open("projects/lib.csv", "r") as library:
        reader = csv.DictReader(library, fieldnames=fieldnames)
        for row in reader:
            if row["title"] == title:
                print(f"Alrighty, you chose to update {title}")
                new_title = input("What is the new title of the book?\n")
                new_author = input("Who is the new author of the book?\n")
                new_year = int(input("What is the new year the book was published?\n"))
                new_genre = input("What is the new genre of the book?\n")
                new_format = input("What is the new format\n e.g. poem or normal\n")
                new_rating = float(input("What is the new rating of the book?\n"))
                new_notes = input("Is there any extra notes you want to add?\n")
                total_inputs = {
                    "title": new_title,
                    "author": new_author,
                    "year": new_year,
                    "genre": new_genre,
                    "format": new_format,
                    "rating": new_rating,
                    "notes": new_notes
                    }
                    
                with open("projects/lib.csv", "w", newline = '') as library:
                    writer = csv.DictWriter(library, fieldnames=fieldnames)
                    for row in reader:
                        if row["title"] != title:
                            writer.writerow(row)
                        else:
                            writer.writerow(total_inputs)
                            print(f"You successfully updated {title} to {new_title}")
                            return main_menu()
        if row["title"] != title:
            print("That ain't a book in your library")
            return main_menu()
        else:
            print("Bruh")
            return main_menu()

def main_menu():
    while True:
        t.sleep(1)
        choice = input("What would you like to do?\n1. Add a book\n2. View all books\n3. Remove a book\n4. Update a book\n5. Exit the program\n")
        if choice == "1":
            add()
        elif choice == "2":
            view()
        elif choice == "3":
            remove()
        elif choice == "4":
            update_item()
        elif choice == "5":
            print("You chose to exit!")
            break
            return
        else:
            print("You can't do that!")
main_menu()