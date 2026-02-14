#4. Write a python program to print the contents of a directory using the os module. 

import os

# Specify the directory (You can replace '.' with any directory path)
directory_path = '/'

try:
    # List all files and folders in the directory
    contents = os.listdir(directory_path)

    print(f"Contents of directory '{directory_path}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print("The specified directory does not exist.")
except PermissionError:
    print("You do not have permission to access this directory.")
