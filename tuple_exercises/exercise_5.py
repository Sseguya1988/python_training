# Exercise 5: Swap two tuples in Python
tuple1 = (11, 22)
tuple2 = (99, 88)
# set up a temporary tuple to do the swap
temp_tuple = tuple1
tuple1 = tuple2
tuple2 = temp_tuple
print(f"tuple1 = {tuple1}")
print(f"tuple2 = {tuple2}")
