def calculate_slope(a, b):
    if b != 0:
        slope = -a / b
        return slope
    else:
        print("The line is vertical (b = 0). Slope is undefined.")
        return None


# Input coefficients
a = float(input("Enter the coefficient 'a': "))
b = float(input("Enter the coefficient 'b': "))

result = calculate_slope(a, b)
if result is not None:
    print(f"The slope of the line is {result:.2f}")
