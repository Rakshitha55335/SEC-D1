# Python program to count the number of vowels in a string

string = input("Enter a string: ")

count = (
    string.count('a') + string.count('e') + string.count('i') +
    string.count('o') + string.count('u') +
    string.count('A') + string.count('E') + string.count('I') +
    string.count('O') + string.count('U')
)

print("Number of vowels:", count)