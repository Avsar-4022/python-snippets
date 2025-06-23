# Function to print the multiplication table
def print_multiplication_table(number):
    print(f"Multiplication table for {number}:")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")


# Prompt the user to input a number
num = int(input("Enter a number: "))

# Print the multiplication table
print_multiplication_table(num)
