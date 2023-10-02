# Exercise 4: Count the occurrence of each element from a list

from collections import Counter
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

item_count = Counter(sample_list)
sample_list_dict = dict(item_count)
print(sample_list_dict)
