# Prompt the user to enter the number of calls
calls = int(input("Enter the number of calls: "))

# Initialize the bill amount
bill = 0

# Calculate the bill based on the number of calls
if calls <= 100:
    bill = 200
elif calls <= 150:
    bill = 200 + (calls - 100) * 0.60
elif calls <= 200:
    bill = 200 + 50 * 0.60 + (calls - 150) * 0.50
else:
    bill = 200 + 50 * 0.60 + 50 * 0.50 + (calls - 200) * 0.40

# Display the bill amount
print(f"The total bill for {calls} calls is Rs. {bill:.2f}")
