def exchange_last_digits_and_multiply(num1, num2):
    # Convert the numbers to strings
    num1_str, num2_str = str(num1), str(num2)

    # Ensure both numbers have at least two digits
    if len(num1_str) < 2 or len(num2_str) < 2:
        print("Please enter numbers with at least two digits.")
        return None

    # Swap the last digits
    modified_num1 = num1_str[:-1] + num2_str[-1]
    modified_num2 = num2_str[:-1] + num1_str[-1]

    # Calculate the product of the modified numbers
    product = int(modified_num1) * int(modified_num2)
    return product


# Example usage:
try:
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    result = exchange_last_digits_and_multiply(number1, number2)
    if result is not None:
        print(f"The product after exchanging last digits: {result}")
except ValueError:
    print("Invalid input. Please enter valid integers.")
