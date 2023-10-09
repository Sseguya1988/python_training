# Exercise 2: Create a 5X2 integer array from a range between 100 to 200 such that the difference between each element is 10
import numpy as np
# create a 5x2 array in required range
array = np.arange(100, 200, 10).reshape(5, 2)

# print array
print("Creating 5X2 array using numpy.arange")
print(array)
