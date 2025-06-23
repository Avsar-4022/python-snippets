# Function to double the second last digit
def double_second_last_digit(number):
    num_str = str(number)
    if len(num_str) < 2:
        return "Number must have at least two digits."

    # Convert the number to a list of characters
    num_list = list(num_str)

    # Double the second last digit
    second_last_digit = int(num_list[-2])
    doubled_digit = second_last_digit * 2

    # Replace the second last digit with the doubled value
    num_list[-2] = str(doubled_digit)

    # Join the list back into a string and convert to an integer
    modified_number = int(''.join(num_list))

    return modified_number


# Taking input from the user
number = int(input("Enter a number: "))

# Doubling the second last digit and displaying the result
result = double_second_last_digit(number)
print("The number after doubling the second last digit is:", result)
