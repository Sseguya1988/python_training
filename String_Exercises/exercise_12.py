# Exercise 12: Find the last position of a given substring
input_string = input("Enter a string with more than one part: ")
# use rfind() to find last position of substring
last_position = input_string.rfind("Emma")
# use if statement
if last_position != -1:
    print(f"The last position of the string 'Emma' is {last_position}")
else:
    print("Emma was not found in this String")
