# Create and open a text file in write mode

file = open("sample.txt", "w")

# Write contents into the file
file.write("Python is easy to learn.\n")
file.write("Python is a programming language.")

# Close the file
file.close()

# Open the file in read mode
file = open("sample.txt", "r")

# Read and display the contents
content = file.read()

print(content)

# Close the file
file.close()