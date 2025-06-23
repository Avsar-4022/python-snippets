# Function to calculate factorial iteratively
def factorial_iterative(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial


# Prompt the user to input a number
num = int(input("Enter a number: "))

# Check if the number is negative
if num < 0:
    print("Sorry, factorial does not exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    print(f"The factorial of {num} is {factorial_iterative(num)}.")
