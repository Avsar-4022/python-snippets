# Function to check voting eligibility
def check_voting_eligibility(age):
    if age >= 18:
        return "You are eligible to vote."
    else:
        return "You are not eligible to vote."


# Taking input from the user
age = int(input("Enter your age: "))

# Checking eligibility and displaying the result
result = check_voting_eligibility(age)
print(result)
