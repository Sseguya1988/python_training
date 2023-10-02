# Exercise 3: Slice list into 3 equal chunks and reverse each chunk
sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
sub_list1 = sample_list[:3]
sub_list2 = sample_list[3:6]
sub_list3 = sample_list[6:]
# reverse items in the lists
for item in [sub_list1, sub_list2, sub_list3]:
    item.reverse()
print("The three lists are as follows;")
print(sub_list1)
print(sub_list2)
print(sub_list3)
