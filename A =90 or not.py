# Function to check if angle A is 90 degrees
def is_angle_A_right(a, b, c):
    # Check if a^2 == b^2 + c^2
    if a**2 == b**2 + c**2:
        return "Angle A is 90°."
    else:
        return "Angle A is not 90°."


# Taking input from the user
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

# Checking if angle A is 90 degrees and displaying the result
result = is_angle_A_right(a, b, c)
print(result)
