# Python program to demonstrate multiple return values

def calculate(a, b):
    sum = a + b
    product = a * b
    return sum, product

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

addition, multiplication = calculate(x, y)

print("Sum =", addition)
print("Product =", multiplication)