# Exercise 10: Create two 2-D arrays and Plot them using matplotlib
import numpy as np
import matplotlib.pyplot as plt


# create two 2-D arrays
array1 = np.array([[1, 0, 8],
                   [2, 9, 2],
                   [7, 1, 3]])
array2 = np.array([[5, 1, 9],
                   [1, 9, 2],
                   [4, 5, 3]])
# create a figure with two subplots
fig, axs = plt.subplots(1, 2)
# plot first array in the first subplot
axs[0].imshow(array1, cmap="viridis")
axs[0].set_title("Array One Figure")

# plot the second array
axs[1].imshow(array2, cmap="plasma")
axs[1].set_title("Array Two Figure")

# show these plots
plt.show()
