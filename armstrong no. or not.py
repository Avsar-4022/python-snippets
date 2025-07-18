# Function to check if a number is an Armstrong number
def is_armstrong_number(number):
    # Convert the number to a string to calculate the number of digits
    num_str = str(number)
    num_digits = len(num_str)

    # Calculate the sum of each digit raised to the power of the number of digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)

    # Check if the sum of powers is equal to the original number
    return sum_of_powers == number


# Prompt the user to input a number
num = int(input("Enter a number: "))

# Check and display if the number is an Armstrong number
if is_armstrong_number(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
