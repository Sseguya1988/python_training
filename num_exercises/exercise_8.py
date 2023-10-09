# Exercise 8: Print max from axis 0 and min from axis 1 from the following 2-D array.
import numpy as np

# state given array
sampleArray = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])
# max from x-axis
max_from_x_axis = np.max(sampleArray, axis=0)
# min from axis =1
min_from_axia_1 = np.min(sampleArray, axis=1)
# print max from x axis
print(f" The maximum from axis 0 is {max_from_x_axis}")
print(f"The minimum from axis 1 is {min_from_axia_1}")
