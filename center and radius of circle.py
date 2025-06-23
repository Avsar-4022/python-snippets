import math


# Function to calculate the center and radius of the circle
def calculate_circle_properties(a, b, c):
    # Center of the circle
    h = -a
    k = -b

    # Radius of the circle
    radius = math.sqrt(h ** 2 + k ** 2 - c)

    return (h, k), radius


# Taking input from the user
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

# Calculating the center and radius
center, radius = calculate_circle_properties(a, b, c)

# Displaying the result
print(f"The center of the circle is: {center}")
print(f"The radius of the circle is: {radius:.1f}")
