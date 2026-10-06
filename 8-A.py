from array import *

# Create an array
arr = array('i', [10, 20, 30, 40])

# Display the array
print("Original array:", arr)

# Append an item
arr.append(50)
print("After append:", arr)

# Insert an item
arr.insert(2, 25)
print("After insert:", arr)

# Reverse the array
arr.reverse()
print("After reverse:", arr)