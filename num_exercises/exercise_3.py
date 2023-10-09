# Exercise 3: Following is the provided numPy array. Return array of items by taking the third column from all rows
import numpy as np

# state the given 3x3 numpy array
sampleArray = np.array([[11, 22, 33], [44, 55, 66], [77, 88, 99]])
# extract second column as array
column_array = sampleArray[:, 1]
# print this array
print(column_array)
