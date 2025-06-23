# Function to swap the last and third last digits
def swap_last_third_last_digits(number):
    num_str = str(number)
    if len(num_str) < 3:
        return "Number must have at least three digits."

    # Convert the number to a list of characters
    num_list = list(num_str)

    # Swap the last and third last digits
    num_list[-1], num_list[-3] = num_list[-3], num_list[-1]

    # Join the list back into a string and convert to an integer
    swapped_number = int(''.join(num_list))

    return swapped_number


# Taking input from the user
number = int(input("Enter a number: "))

# Swapping the digits and displaying the result
result = swap_last_third_last_digits(number)
print("The number after swapping the last and third last digits is:", result)
