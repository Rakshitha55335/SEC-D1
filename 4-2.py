# Python program to check whether a substring is present

string = input("Enter a string: ")
substring = input("Enter the substring: ")

if substring in string:
    print("Substring is present in the string")
else:
    print("Substring is not present in the string")