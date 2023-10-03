# Exercise 8: Sort a tuple of tuples by 2nd item
tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
# sort the tuple
sorted_tuple = sorted(tuple1, key=lambda i: i[1])
print(sorted_tuple)
