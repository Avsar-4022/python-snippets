# Function to calculate the sum of squares of the first n natural numbers
def sum_of_squares(n):
    return (n * (n + 1) * (2 * n + 1)) // 6


# Prompt the user to input a number
num = int(input("Enter a number: "))

# Calculate and display the sum of squares
print(f"The sum of squares of the first {num} natural numbers is {sum_of_squares(num)}.")
