# Create a tuple with repeated items

my_tuple = (10, 20, 30, 20, 40, 10, 50, 30)

# Find repeated items
repeated = set()

for item in my_tuple:
    if my_tuple.count(item) > 1:
        repeated.add(item)

# Display repeated items
print("Repeated items:", repeated)