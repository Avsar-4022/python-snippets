# Function to calculate the sum of digits
def sum_of_digits(number):
    total = 0
    while number > 0:
        digit = number % 10
        total += digit
        number //= 10
    return total


# Prompt the user to input a number
num = int(input("Enter a number: "))

# Calculate and display the sum of digits
print(f"The sum of the digits of {num} is {sum_of_digits(num)}.")
