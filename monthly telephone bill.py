# Prompt the user to input the number of calls
calls = int(input("Enter the number of calls: "))

# Initialize the bill amount
bill = 200  # Minimum charge for up to 100 calls

# Calculate the bill based on the number of calls
if calls > 100:
    if calls <= 150:
        bill += (calls - 100) * 0.60
    elif calls <= 200:
        bill += 50 * 0.60 + (calls - 150) * 0.50
    else:
        bill += 50 * 0.60 + 50 * 0.50 + (calls - 200) * 0.40

# Display the total bill
print(f"The total bill is Rs. {bill:.2f}")
