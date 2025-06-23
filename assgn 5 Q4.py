# Function to determine the value of Y based on X
def calculate_Y(X):
    if X == 6:
        return X + 10
    elif X == 7:
        return X * X
    elif X == 12:
        return 2 * X + 4
    else:
        return X * 6 - 1


# Taking input from the user
X = int(input("Enter the value of X: "))

# Calculating Y and displaying the result
Y = calculate_Y(X)
print("The value of Y is:", Y)
