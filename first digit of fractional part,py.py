# Function to find the first digit of the fractional part
def first_digit_fractional_part(number):
    # Convert the number to a string
    num_str = str(number)

    # Check if there is a decimal point
    if '.' in num_str:
        # Split the number into integer and fractional parts
        integer_part, fractional_part = num_str.split('.')

        # Return the first digit of the fractional part
        return fractional_part[0]
    else:
        return "The number has no fractional part."


# Taking input from the user
number = float(input("Enter a number: "))

# Finding the first digit of the fractional part and displaying the result
result = first_digit_fractional_part(number)
print("The first digit of the fractional part is:", result)
7