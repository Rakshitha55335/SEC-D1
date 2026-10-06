# Python program to check a leap year using a function

def isLeap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

year = int(input("Enter a year: "))

if isLeap(year):
    print(year, "is a Leap Year.")
else:
    print(year, "is Not a Leap Year.")