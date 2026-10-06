# Python program to find the length of a string without using library functions

string = input("Enter a string: ")

count = 0

for char in string:
    count = count + 1

print("Length of the string:", count)