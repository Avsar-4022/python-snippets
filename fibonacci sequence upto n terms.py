# Function to generate Fibonacci sequence
def fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


# Prompt the user to input the number of terms
num_terms = int(input("Enter the number of terms: "))

# Check if the number of terms is valid
if num_terms <= 0:
    print("Please enter a positive integer.")
else:
    print(f"Fibonacci sequence up to {num_terms} terms:")
    print(fibonacci_sequence(num_terms))
