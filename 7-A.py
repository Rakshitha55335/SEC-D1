# Read words from the source file

with open("source.txt", "r") as file:
    words = file.read().split()

# Convert words to lowercase and sort them
words = [word.lower() for word in words]
words.sort()

# Write sorted words into another file
with open("output.txt", "w") as file:
    file.write("\n".join(words))

print("Words sorted and written to output.txt")