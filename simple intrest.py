#Program to print the simple intrest taking pronciple,rate and time as inputs from the user
#Input from the user
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (in percentage): "))
time = float(input("Enter the time (in years): "))
# Calculate and print the simple interest
simple_intrest = (principal*rate*time)/100
print("The simple intrest is: ",simple_intrest)