# Get the lengths of the three sides of the triangle from the user
s1 = float(input("Enter the first side of the triangle: "))
s2 = float(input("Enter the second side of the triangle: "))
s3 = float(input("Enter the third side of the triangle: "))

# Calculate the perimeter
p = s1 + s2 + s3

# Calculate the semi-perimeter
s = p / 2

# Calculate the area using Heron's formula
area = (s * (s - s1) * (s - s2) * (s - s3)) ** 0.5

# Print the results
print(f"The perimeter of the triangle is: {p:.2f}")
print(f"The area of the triangle is: {area:.2f}")
