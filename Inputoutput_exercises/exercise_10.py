# Exercise 10: Read line number 4 from the following file
# open a .txt file
content = "\n".join(f"line{i}" for i in range(1, 8))
# create a .txt file
with open("test.txt", "w") as test_file:
    test_file.write(content)
# define the file path
file_path = "test.txt"
# line number to read
read_line_number = 4
# Variable to store line read
Line_to_read = None
# Open file in read mode
with open(file_path, "r") as file:
    # iterate through the line numbers
    for i, line in enumerate(file, start=1):
        if i == read_line_number:
            line_to_read = line
            break
    print(f"Line {read_line_number}: {line_to_read}")




