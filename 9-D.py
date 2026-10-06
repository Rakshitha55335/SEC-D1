import numpy as np

# Create a NumPy array
arr = np.array([10, 20, 30, 40, 50])

print("Original array:", arr)

# Basic slicing
print("Basic slicing:", arr[1:4])

# Integer indexing
print("Integer indexing:", arr[[0, 2, 4]])

# Boolean indexing
print("Boolean indexing:", arr[arr > 25])