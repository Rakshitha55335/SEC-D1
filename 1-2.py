# Python program to demonstrate operators

a = 10
b = 5

# Arithmetic Operators
print("Arithmetic Operators")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)

# Relational Operators
print("\nRelational Operators")
print("a > b:", a > b)
print("a < b:", a < b)
print("a == b:", a == b)
print("a != b:", a != b)

# Assignment Operators
print("\nAssignment Operators")
x = 10
print("x =", x)

x += 5
print("x += 5:", x)

x -= 3
print("x -= 3:", x)

x *= 2
print("x *= 2:", x)

# Logical Operators
print("\nLogical Operators")
print("a > b and b > 0:", a > b and b > 0)
print("a > b or b < 0:", a > b or b < 0)
print("not(a > b):", not(a > b))

# Bitwise Operators
print("\nBitwise Operators")
print("a & b:", a & b)
print("a | b:", a | b)
print("a ^ b:", a ^ b)
print("a << 1:", a << 1)
print("a >> 1:", a >> 1)

# Ternary Operator
print("\nTernary Operator")
result = "a is greater" if a > b else "b is greater"
print(result)

# Membership Operators
print("\nMembership Operators")
numbers = [1, 2, 3, 4, 5]
print("3 in numbers:", 3 in numbers)
print("10 not in numbers:", 10 not in numbers)

# Identity Operators
print("\nIdentity Operators")
p = [1, 2, 3]
q = p
r = [1, 2, 3]

print("p is q:", p is q)
print("p is r:", p is r)
print("p is not r:", p is not r)