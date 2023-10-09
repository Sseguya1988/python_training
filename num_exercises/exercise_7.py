# Exercise 7: Sort following NumPy array
import numpy as np

# state the numpy array to use
sampleArray = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])
# extract row to use in sorting
sort_row = np.argsort(sampleArray[1])
# form sorted array
row_sorted_array = sampleArray[:, sort_row]
# for column array for sorting
column_sort = np.argsort(sampleArray[:, 1])
# form column sorted array
column_sorted = sampleArray[column_sort]
# print original array
print(f"Original array is: \n{sampleArray}")
# print column sorted array
print(f"The column sorted array is: \n{column_sorted}")
# print row sorted array
print(f"The row sorted array is: \n{row_sorted_array}")
