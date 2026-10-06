import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["Akhil", "Bhavana", "Charan", "Divya", "Eswar"],
    "Age": [20, 21, 20, 22, 21],
    "Marks": [85, 91, 88, 95, 90],
    "Branch": ["CSE", "ECE", "CSE", "EEE", "CSE"]
}

df = pd.DataFrame(data)

# Select two columns
x = df["Age"]
y = df["Marks"]

print("Selected Age column:")
print(x)

print("\nSelected Marks column:")
print(y)

# Scatter plot
plt.scatter(x, y)
plt.xlabel("Age")
plt.ylabel("Marks")
plt.title("Age vs Marks")
plt.show()