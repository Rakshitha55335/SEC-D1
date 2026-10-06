# Check whether list elements exist as values in a dictionary

numbers = [10, 20, 30, 40, 50]

data = {
    "a": 10,
    "b": 30,
    "c": 50
}

for num in numbers[:]:
    if num not in data.values():
        numbers.remove(num)

print("Updated list:", numbers)