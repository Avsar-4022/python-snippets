def sum_last_two_digits(n):
    num_str = str(n)
    if len(num_str) < 2:
        print("Invalid input. Please enter a number with at least two digits.")
        return None

    last_digit = int(num_str[-1])
    second_last_digit = int(num_str[-2])
    return last_digit + second_last_digit


# Example usage:
try:
    number = int(input("Enter a number: "))
    result = sum_last_two_digits(number)
    if result is not None:
        print(f"The sum of the last two digits of {number} is {result}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
