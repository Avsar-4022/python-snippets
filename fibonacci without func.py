# Prompt the user to enter the number of terms
num_terms = int(input("Enter the number of terms: "))

# Initialize the first two terms
first_term = 0
second_term = 1

# Check if the number of terms is valid
if num_terms <= 0:
    print("Please enter a positive integer.")
elif num_terms == 1:
    print(f"Fibonacci sequence up to {num_terms} term: {first_term}")
else:
    print("Fibonacci sequence:")
    print(first_term, second_term, end=" ")
    for _ in range(2, num_terms):
        next_term = first_term + second_term
        print(next_term, end=" ")
        first_term = second_term
        second_term = next_term
