# Input three numbers separated by commas
numbers_str = input("Enter three numbers separated by commas: ")

# Convert the input string to a list of floats
numbers_list = [float(num) for num in numbers_str.split(',')]

# Find the largest and smallest numbers
largest = max(numbers_list)
smallest = min(numbers_list)

# Print the results
print(f"The largest number is {largest:.2f}")
print(f"The smallest number is {smallest:.2f}")
