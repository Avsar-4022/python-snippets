def print_last_digit(number):
    last_digit = number % 10
    print(f"The last digit of {number} is {last_digit}")


# Example usage:
user_number = int(input("Enter a number: "))
print_last_digit(user_number)
