# Python program to calculate the sum of digits

num = int(input("Enter a number: "))

original = num
sum_digits = 0

while num > 0:
    digit = num % 10
    sum_digits = sum_digits + digit
    num = num // 10

print("Sum of the digits of", original, "=", sum_digits)