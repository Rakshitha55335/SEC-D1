# Python program to create a new list
# by picking odd-index items from the first list
# and even-index items from the second list

list1 = [10, 20, 30, 40, 50]
list2 = [60, 70, 80, 90, 100]

new_list = []

# Pick odd-index items from list1
for i in range(1, len(list1), 2):
    new_list.append(list1[i])

# Pick even-index items from list2
for i in range(0, len(list2), 2):
    new_list.append(list2[i])

print("First list:", list1)
print("Second list:", list2)
print("New list:", new_list)