# Exercise 7: Add new item to list after a specified item
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# define sublist containing 6000
sub_list_6000 = list1[2][2]
# modify this sublist to add 7000
sub_list_6000.append(7000)
print(list1)
