# Exercise 2: Concatenate two lists index-wise
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
# create an empty list to store new combined items
combined_list = [x + y for x, y in zip(list1, list2)]
print(combined_list)

