def get_second_last_digit(num):
    return abs(num) // 10 % 10


# Example usage:
number = int(input("Enter a number: "))
second_last_digit = get_second_last_digit(number)
print(f"The second-to-last digit of {number} is {second_last_digit}")
