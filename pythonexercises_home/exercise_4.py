# Exercise 4: Reverse Dictionary mapping
ascii_dict = {"A": 65, "B": 66, "C": 67, "D": 68}
reverse_dict = {}
for key, value in ascii_dict.items():
    reverse_dict[value]=key
print(reverse_dict)
