# Create a list of tuples

my_list = [(1, "Akhil"), (2, "Bhavana"), (3, "Charan")]

# Unzip the list of tuples into individual lists
numbers, names = zip(*my_list)

# Convert them into lists
numbers = list(numbers)
names = list(names)

# Display the individual lists
print("First List:", numbers)
print("Second List:", names)