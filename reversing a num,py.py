# Function to reverse a number
def reverse_number(number):
    reversed_num = 0
    while number > 0:
        digit = number % 10
        reversed_num = reversed_num * 10 + digit
        number //= 10
    return reversed_num


# Prompt the user to input a number
num = int(input("Enter a number: "))

# Calculate and display the reversed number
print(f"The reversed number is {reverse_number(num)}.")
