# Python program to demonstrate local and global variables

# Global variable
x = 100

def display():
    # Local variable
    y = 50

    print("Inside Function")
    print("Global Variable x =", x)
    print("Local Variable y =", y)

# Function call
display()

print("\nOutside Function")
print("Global Variable x =", x)

# The following line will generate an error
# print("Local Variable y =", y)