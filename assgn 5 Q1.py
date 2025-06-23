# Function to perform operations based on the value of X
def perform_operation(X, Y, Z):
    if X == 0:
        return Y + Z
    elif X == 1:
        return Y - Z
    elif X == 2:
        return Y * Z
    elif X == 3:
        return Y / Z
    else:
        return "Invalid value for X"


# Taking input from the user
X = int(input("Enter the value of X (0, 1, 2, or 3): "))
Y = int(input("Enter the value of Y: "))
Z = int(input("Enter the value of Z: "))

# Performing the operation and displaying the result
result = perform_operation(X, Y, Z)
print("The result is:", result)
