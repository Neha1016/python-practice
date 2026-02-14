import os

# Specify the directory (You can replace '.' with any directory path)
directory_path = '/'

try:
    # list all the files that in my computer
    contents = os.listdir(directory_path)

    print(f"Contents of directory '{directory_path}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print("The specified directory does not exist.")
except PermissionError:
    print("You do not have permission to access this directory.")
