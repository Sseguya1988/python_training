# Exercise 10: Create a new list from two list using the following condition

# state given lists
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
# create an empty list
new_list = []

# iterate through list1
for num in list1:
    if num % 2 != 0:
        new_list.append(num)

# iterate through second list
for num in list2:
    if num % 2 == 0:
        new_list.append(num)

# print the new list
print(new_list)

