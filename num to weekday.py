# Define a list of days
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# Prompt the user to enter a number between 1 and 7
number = int(input("Enter a number from 1 to 7: "))

# Check if the number is within the valid range
if 1 <= number <= 7:
    # Display the corresponding day
    print(f"The day corresponding to number {number} is {days[number - 1]}.")
else:
    print("Please enter a valid number between 1 and 7.")
