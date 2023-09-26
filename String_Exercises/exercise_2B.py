# Exercise 2: Append new string in the middle of a given string
def create_string(s1, s2):
    length_s1 = len(s1)
    middle_index = length_s1 // 2

    # construct new string
    new_string = s1[:middle_index] + s2 + s1[middle_index:]
    return new_string


# apply this function
s1 = input("Enter your first string: ")
s2 = input("Enter your second string: ")

result = create_string(s1, s2)
print(result)
