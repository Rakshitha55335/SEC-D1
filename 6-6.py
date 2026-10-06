# Create a list

my_list = [10, 20, 30, 40, (50, 60), 70, 80]

# Count elements until a tuple is found
count = 0

for item in my_list:
    if isinstance(item, tuple):
        break

    count = count + 1

# Display the count
print("Number of elements before the tuple:", count)