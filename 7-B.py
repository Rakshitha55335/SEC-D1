# Open the file in read mode

with open("source.txt", "r") as file:
    lines = file.readlines()

# Print each line in reverse order
for line in lines:
    print(line.strip()[::-1])