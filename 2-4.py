# Python program to check a Perfect Number

num = int(input("Enter a number: "))

sum = 0

for i in range(1, num):
    if num % i == 0:
        sum = sum + i

if sum == num:
    print(num, "is a Perfect Number.")
else:
    print(num, "is not a Perfect Number.")