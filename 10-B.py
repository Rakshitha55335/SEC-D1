import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Ask the user to guess
guess = int(input("Guess a number between 1 and 10: "))

# Check the guess
if guess == secret_number:
    print("Congratulations! You guessed the correct number.")
else:
    print("Wrong guess!")
    print("The correct number was:", secret_number)