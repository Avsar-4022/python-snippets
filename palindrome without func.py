# Prompt the user to enter a number
number = int(input("Enter a number: "))

# Store the original number
original_number = number

# Initialize the reversed number to 0
reversed_number = 0

# Reverse the number
while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10

# Check if the original number is equal to the reversed number
if original_number == reversed_number:
    print(f"{original_number} is a palindrome.")
else:
    print(f"{original_number} is not a palindrome.")
