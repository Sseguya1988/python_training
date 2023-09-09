# Exercise 4: Reverse Dictionary mapping
ascii_dict = {"A": 65, "B": 66, "C": 67, "D": 68}
# Create empty dictionary
reverse_dict = {}
# Use a for loop to re-assign elements in the set
for key, value in ascii_dict.items():
    reverse_dict[value] = key
# print new dictionary
print(reverse_dict)
