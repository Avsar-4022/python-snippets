# Prompt the user to enter a number
number = int(input("Enter a number: "))

# Initialize an empty list to store the factors
factors = []

# Loop through all numbers from 1 to the given number
for i in range(1, number + 1):
    if number % i == 0:
        factors.append(i)

# Display the factors
print(f"The factors of {number} are: {factors}")
