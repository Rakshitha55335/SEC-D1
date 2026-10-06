# Python program to check whether a number is a palindrome

def isPalindrome(number):
    original = number
    reverse = 0

    while number > 0:
        digit = number % 10
        reverse = reverse * 10 + digit
        number = number // 10

    return original == reverse

num = int(input("Enter a number: "))

if isPalindrome(num):
    print(num, "is a Palindrome Number.")
else:
    print(num, "is Not a Palindrome Number.")