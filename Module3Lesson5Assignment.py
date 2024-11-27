"""
1. Exploring Python's OS Module

Task 1: Directory Inspector:

Problem Statement: Create a Python script that lists all files and subdirectories in a given directory. 
Your script should prompt the user for the directory path and then display the contents.

Expected Outcome: The script should correctly list all files and subdirectories in the specified directory. 
Handle exceptions for invalid paths or inaccessible directories.

"""

import os

def list_directory_contents(path):
    try:
        print(f"Directory Contents: \n{"*"*20}" )
        for line in os.listdir(path):
            print(line)
    except IOError as e:
        print(f"An error occurred: {e}")
    except PermissionError as e:
        print(f"Permission Error. Check your path.")
    except FileNotFoundError as e:
        print(f"File not found. Check your path.")
    except Exception as e:
        print(f"An unexpected error has occurred: {e}")

path = input("Please input the file path: ")

list_directory_contents(path)