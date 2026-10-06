import pandas as pd

# Create a dictionary
data = {
    "Name": ["Akhil", "Bhavana", "Charan", "Divya", "Eswar",
             "Farah", "Ganesh", "Harika", "Isha", "Kiran"],
    "Age": [20, 21, 20, 22, 21, 20, 22, 21, 20, 22],
    "Marks": [85, 91, 88, 95, 90, 80, 89, 93, 87, 92]
}

# Convert dictionary into DataFrame
df = pd.DataFrame(data)

# Display first 5 rows
print("First 5 rows of the DataFrame:")
print(df.head())