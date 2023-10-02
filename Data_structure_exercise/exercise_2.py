# Exercise 2: Remove and add item in a list
sample_list = [1, 2, 3, 4, 5]
# use pop to remove item at index 4
removed_item = sample_list.pop(4)
# insert removed item to second position
sample_list.insert(1, removed_item)
# add removed item to the list using append
sample_list.append(removed_item)
# print the new list
print(sample_list)
