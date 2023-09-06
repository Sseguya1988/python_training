# Exercise 2: Read text file into a variable and replace all newlines with space

# Write data in sample.txt
# Open a txt file and name it
file = open("sample.txt", "w")
# write in sample.txt
file.write("line1\n")
file.write("line2\nline3\n")
file.write("line4\n")
file.write("line5\n")
# file.close # this closing command is optional for this python version

# Reading from this text file
file = open("sample.txt", "r")
data = file.readlines()
# creating an empty list
new_list = []
# Removing the last \n character on the items
for i in data:
    if i[-1] == "\n":
        new_list.append(i[:-1])
    else:
        new_list.append(i)
# Joining items into one line
sentence = " ".join(new_list)
print(sentence)
