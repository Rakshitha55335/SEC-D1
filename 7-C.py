# Open the file in read mode

with open("source.txt", "r") as file:
    content = file.read()

# Count characters, words and lines
characters = len(content)
words = len(content.split())
lines = len(content.splitlines())

# Display the results
print("Number of characters:", characters)
print("Number of words:", words)
print("Number of lines:", lines)