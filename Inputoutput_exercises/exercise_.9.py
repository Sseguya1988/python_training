# Exercise 9: Check file is empty or not
# Specify the file path
import os

# Specify the file path
file_path = "destination1.txt"

# Check if the file exists
if os.path.exists(file_path):
    # Get the size of the file
    file_size = os.path.getsize(file_path)

    # Check if the file size is empty
    if file_size == 0:
        print(f"The file '{file_path}' is empty.")
    else:
        print(f"The file '{file_path}' is not empty. It has a size of {file_size} bytes.")
else:
    print(f"The file '{file_path}' does not exist.")

