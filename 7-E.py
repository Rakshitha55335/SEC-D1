# Open the source file in read mode

file = open("source.txt", "r")

# Read the contents of the file
content = file.read()

# Get the character to remove
ch = input("Enter the character to remove: ")

# Count the occurrences of the character
count = content.count(ch)

# Remove all occurrences of the character
new_content = content.replace(ch, "")

# Close the source file
file.close()

# Open another file in write mode
file = open("result.txt", "w")

# Write the modified content into the new file
file.write(new_content)

# Close the result file
file.close()

# Display the count and modified content
print("Total occurrences of", ch, ":", count)
print("Resultant text:")
print(new_content)