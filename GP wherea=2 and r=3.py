# Function to generate the first n terms of a geometric sequence
def geometric_sequence(start, ratio, terms):
    sequence = []
    current_term = start
    for _ in range(terms):
        sequence.append(current_term)
        current_term *= ratio
    return sequence


# Define the starting term, common ratio, and number of terms
start_term = 2
common_ratio = 3
num_terms = 6

# Generate and display the geometric sequence
sequence = geometric_sequence(start_term, common_ratio, num_terms)
print(f"The first {num_terms} terms of the geometric sequence are: {sequence}")
