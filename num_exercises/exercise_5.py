# Exercise 5: Create a result array by adding the following two NumPy arrays. Next, modify the result array by calculating the square of each element
import numpy as np

# state given numpy arrays to operate on
arrayOne = np.array([[5, 6, 9], [21, 18, 27]])
arrayTwo = np.array([[15, 33, 24], [4, 7, 1]])
# result array
addition_result = np.add(arrayOne, arrayTwo)
# calculate square of each element
squared_element_array = np.square(addition_result)
# print result array
print(addition_result)
print("Result array after calculating the square root of all elements")
print(squared_element_array)

