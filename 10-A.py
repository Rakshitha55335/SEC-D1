import time

# Get countdown time from the user
seconds = int(input("Enter countdown time in seconds: "))

# Countdown
while seconds > 0:
    minutes = seconds // 60
    remaining_seconds = seconds % 60

    print(f"{minutes:02d}:{remaining_seconds:02d}")

    time.sleep(1)
    seconds = seconds - 1

print("Time's up!")