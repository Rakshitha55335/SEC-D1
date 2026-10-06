import pandas as pd

data = {
    "Name": ["Akhil", "Bhavana", "Charan", "Divya", "Eswar"],
    "Age": [20, 21, 20, 22, 21],
    "Marks": [85, 91, 88, 95, 90],
    "Branch": ["CSE", "ECE", "CSE", "EEE", "CSE"]
}

df = pd.DataFrame(data)

print("Complete DataFrame:")
print(df)

print("\nSelect Name column:")
print(df["Name"])

print("\nSelect Name and Marks columns:")
print(df[["Name", "Marks"]])

print("\nSelect first 3 rows:")
print(df.iloc[0:3])

print("\nSelect row at index 2:")
print(df.iloc[2])

print("\nSelect students with Marks greater than 90:")
print(df[df["Marks"] > 90])

print("\nSelect students from CSE branch:")
print(df[df["Branch"] == "CSE"])