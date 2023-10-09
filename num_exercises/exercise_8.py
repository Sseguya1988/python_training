import numpy as np

# Create a NumPy array
sampleArray = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])

# Get the sorted indices based on the second column (column index 1)
sorted_indices = np.argsort(sampleArray[:, 1])

# Use the sorted indices to reorder the rows of the original array
sorted_array = sampleArray[sorted_indices]

# Print the sorted array
print(sampleArray)
print("Sorted array based on the second column:")
print(sorted_array)
