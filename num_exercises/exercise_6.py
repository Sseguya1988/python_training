# Exercise 6: Split the array into four equal-sized sub-arrays
import numpy as np

# create a 8x3 numpy array
created_array = np.arange(10, 34, 1).reshape(8, 3)
# print 8x3 array
print(created_array)
# split this into four equal sized sub=-arrays
sub_arrays = np.array_split(created_array, 4)
# print these sub-arrays
for i, sub_array in enumerate(sub_arrays):
    print(f"Subarray {i + 1}: \n{sub_array}")
