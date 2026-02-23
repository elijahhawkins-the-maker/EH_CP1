#EHCP2 file functions
from get_time import get_time

def view_info():
    while True:
        file = input("Please write the exact file path to view the file info\n")
        try:
            with open(file, "r") as f:
                content = f.read()
                new_lines = content.count('\n') + 1
                print("File Info:")
                print(f"File Path: {file}")
                print(f"File Size: {len(content)} characters")
                print(f"Number of Lines: {new_lines}")
                print(f"Number of Words: {len(content.split())}")
                break
        except FileNotFoundError:
            print("File not found. Please try again.")

def view_content():
    while True:
        file = input("Please write the exact file path to view the file content\n")
        try:
            with open(file, "r") as f:
                content = f.read()
                print("File Content:")
                print(content)
                break
        except FileNotFoundError:
            print("File not found. Please try again.")

def edit_file():
    while True:
        file = input("Please write the exact file path to edit the file content\n")
        try:
            with open(file, "a") as f:
                new_content = input("Please write the new content to add to the file\n")
                f.write(" " + new_content)
                print(f"File content updated successfully.\nTime updated: {get_time()}")
                f.write(f"\n\nTime Updated: {get_time()}")
                break
        except FileNotFoundError:
            print("File not found. Please try again.")