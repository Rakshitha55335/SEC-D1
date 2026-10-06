# Python program to convert temperatures

print("Temperature Conversion")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print("Temperature in Fahrenheit =", fahrenheit, "°F")

elif choice == 2:
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print("Temperature in Celsius =", celsius, "°C")

else:
    print("Invalid Choice!")