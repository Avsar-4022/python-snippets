import math


# Function to check if a number is a Krishnamurthy number
def is_krishnamurthy_number(number):
    sum_of_factorials = 0
    temp = number

    # Calculate the sum of the factorials of the digits
    while temp > 0:
        digit = temp % 10
        sum_of_factorials += math.factorial(digit)
        temp //= 10

    # Check if the sum of factorials is equal to the original number
    return sum_of_factorials == number


# Prompt the user to input a number
num = int(input("Enter a number: "))

# Check and display if the number is a Krishnamurthy number
if is_krishnamurthy_number(num):
    print(f"{num} is a Krishnamurthy number.")
else:
    print(f"{num} is not a Krishnamurthy number.")
