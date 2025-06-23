# Input from the user


principal = (input("Enter the principal amount: "))
rate = (input("Enter the rate of interest: "))
time = (input("Enter the time in years: "))
# Calculate the amount
amount = int( principal * (pow(((1 + rate) / 100), time) ) )


# Calculate compound interest
compound_intrest = int ( amount - principal )

print("Compound interest is ", compound_intrest)

