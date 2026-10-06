import pandas as pd

# Create a dictionary
data = {
    "Name": ["Akhil", "Bhavana", "Charan", "Divya", "Eswar",
             "Farah", "Ganesh", "Harika", "Isha", "Kiran"],
    "Age": [20, 21, 20, 22, 21, 20, 22, 21, 20, 22],
    "Marks": [85, 91, 88, 95, 90, 80, 89, 93, 87, 92],
    "Branch": ["CSE", "ECE", "CSE", "EEE", "CSE",
               "ECE", "CSE", "IT", "ECE", "CSE"],
    "City": ["Hyderabad", "Delhi", "Mumbai", "Chennai", "Pune",
             "Kolkata", "Bangalore", "Hyderabad", "Delhi", "Pune"]
}

# Convert dictionary into DataFrame
df = pd.DataFrame(data)

# Display DataFrame
print("DataFrame:")
print(df)

# Explore the data
print("\nFirst 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())

print("\nDataFrame information:")
print(df.info())

print("\nStatistical description:")
print(df.describe())

print("\nNumber of rows and columns:")
print(df.shape)

print("\nColumn names:")
print(df.columns)