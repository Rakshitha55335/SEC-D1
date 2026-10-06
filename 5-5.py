# Count the occurrence of each element in a list

numbers = [1, 2, 2, 3, 1, 4, 2, 3]

count = {}

for num in numbers:
    count[num] = count.get(num, 0) + 1

print("Occurrence of each element:", count)