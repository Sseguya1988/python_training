# Exercise 1: Create a 4X2 integer array and Prints its attributes
import numpy as np
# use unsigned int16 data to create a 4x2 integer array
array = np.array([[1, 2], [0, 5], [15, 7], [10, 2]], dtype=np.uint16)

# print Array attributes
print("Printing Array")
print(array)

# Printing Numpy array Attributes
print(f"Array shape is: {array.shape}")  # prints the shape of the array

print(f"Array dimensions are: {array.ndim}")  # prints dimensions of the array

print(f"Length of each element of the array in bytes is: {array.itemsize}")
