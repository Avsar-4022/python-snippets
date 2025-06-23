# Function to check if a number is a palindrome
def is_palindrome(number):
    # Convert the number to a string
    str_num = str(number)
    # Check if the string is equal to its reverse
    return str_num == str_num[::-1]


# Prompt the user to input a number
num = int(input("Enter a number: "))

# Check and display if the number is a palindrome
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
