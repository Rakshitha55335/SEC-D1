# Python program to calculate the factorial of a number

num = int(input("Enter a positive integer: "))

factorial = 1

if num < 0:
    print("Factorial does not exist for negative numbers.")
else:
    for i in range(1, num + 1):
        factorial = factorial * i

    print("Factorial of", num, "=", factorial)