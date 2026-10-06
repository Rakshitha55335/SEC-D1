# Python program to display prime numbers within an interval

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print("\nPrime Numbers:")

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num, end=" ")