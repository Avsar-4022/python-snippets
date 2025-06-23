# Function to find the smallest of three numbers
def find_smallest(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c


# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Finding the smallest number
smallest = find_smallest(num1, num2, num3)

# Displaying the result
print("The smallest number is:", smallest)
