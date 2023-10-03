# Exercise 10: Remove all occurrences of a specific item from a list.
list1 = [5, 20, 15, 20, 25, 50, 20]
new_list = [item for item in list1 if item != 20]
print(new_list)
