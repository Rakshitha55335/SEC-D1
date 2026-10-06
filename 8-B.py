# Read the size of matrices
r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

# Read first matrix
print("Enter elements of first matrix:")
A = []

for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input()))
    A.append(row)

# Read second matrix
print("Enter elements of second matrix:")
B = []

for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input()))
    B.append(row)

# Addition
add = []

for i in range(r):
    row = []
    for j in range(c):
        row.append(A[i][j] + B[i][j])
    add.append(row)

print("Addition of two matrices:")
for row in add:
    print(row)

# Transpose
transpose = []

for j in range(c):
    row = []
    for i in range(r):
        row.append(A[i][j])
    transpose.append(row)

print("Transpose of first matrix:")
for row in transpose:
    print(row)

# Multiplication
multiply = []

for i in range(r):
    row = []
    for j in range(c):
        total = 0
        for k in range(c):
            total = total + A[i][k] * B[k][j]
        row.append(total)
    multiply.append(row)

print("Multiplication of two matrices:")
for row in multiply:
    print(row)