# Python program to demonstrate default arguments

def calculate_area(length, width=10):
    area = length * width
    return area

length = int(input("Enter the length: "))

choice = input("Do you want to enter width? (yes/no): ")

if choice.lower() == "yes":
    width = int(input("Enter the width: "))
    result = calculate_area(length, width)
else:
    result = calculate_area(length)

print("Area =", result)