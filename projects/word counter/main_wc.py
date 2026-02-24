#EHCP2

import time as t
from file_functions import view_info, view_content, edit_file

def main_menu():
    print("Welcome to the Document Manager!")
    while True:
        choice = int(input("What would you like to do?\n1. View the info of a txt file\n2. View the file content\n3. Edit the txt file\n4. Exit\n"))
        if choice == 1:
            t.sleep(1)
            view_info()
        elif choice == 2:
            t.sleep(1)
            view_content()
        elif choice == 3:
            t.sleep(1)
            edit_file()
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

main_menu()