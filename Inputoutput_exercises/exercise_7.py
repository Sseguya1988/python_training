# Exercise 7: Accept any three string from one input() call
str_input = input("Enter three string: ")
input_str = str_input.split()
# use if statement to print result
if len(input_str) == 3:
    string1, string2, string3 = input_str
    print("Name1", string1)
    print("Name2", string2)
    print("Name3", string3)
else:
    print("Enter exactly three names.")

