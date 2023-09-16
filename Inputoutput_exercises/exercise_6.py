# Exercise 6: Write all content of a given file into a new file by skipping line number 5
# Open a .txt file
original_content = "\n".join(f"line{i}" for i in range(1, 8))
# create a source file for writing
with open("original_file.txt", "w") as original_file:
    original_file.write(original_content)
# open a source file for reading
with open("original_file.txt", "r") as original_file:
    # read the original file
    original_content = original_file.read()
    # remove line5 in destination file
    modified_content = "\n".join(line for line in original_content.split("\n") if line != "line5")
# open destination file for writing
with open("destination1.txt", "w") as destination_file:
    destination_file.write(modified_content)
print("File copied successfully.")



