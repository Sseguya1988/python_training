# Exercise 9: Delete the second column from a given array and insert the following new column in its place.
import numpy as np

# state the given arrays
sampleArray = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])
newColumn = np.array([[10, 10, 10]])
# specify the column to delete
column_deleted = 1
# modified array
sampleArray = np.delete(sampleArray, column_deleted, axis=1)
# replace deleted column in numpy array
new_modified_array = np.insert(sampleArray, column_deleted, newColumn, axis=1)
print(new_modified_array)
