# Function to find factors of a number
def find_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors


# Prompt the user to input a number
num = int(input("Enter a number: "))

# Calculate and display the factors
factors = find_factors(num)
print(f"The factors of {num} are: {factors}")
