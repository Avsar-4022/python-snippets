# Prompt the user to enter a number
number = int(input("Enter a number: "))

# Initialize the factorial variable
factorial = 1

# Calculate the factorial using a loop
if number < 0:
    print("Sorry, factorial does not exist for negative numbers.")
elif number == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1, number + 1):
        factorial *= i
    print(f"The factorial of {number} is {factorial}.")
