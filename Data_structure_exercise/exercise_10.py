# Exercise 10: Remove duplicates from a list and create a tuple and find the minimum and maximum number
sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
# remove duplicates by converting this into a set and back to list
unique_items = list(set(sample_list))
# create a tuple from unique_items
unique_tuple = tuple(unique_items)
# find the maximum and minimum numbers in the tuple
max_number = max(unique_tuple)
mini_number = min(unique_tuple)
# print results
print(f"List with removed duplicates is : {unique_items}")
print(f"Created tuple is: {unique_tuple}")
print(f"maximum number in tuple is {max_number} and minimum number is {mini_number}")
