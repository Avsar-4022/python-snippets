import math

# Function to calculate the volume of a cone
def calculate_cone_volume(radius, height):
    volume = (1/3) * math.pi * (radius ** 2) * height
    return volume


# Taking input from the user
radius = float(input("Enter the radius of the cone: "))
height = float(input("Enter the height of the cone: "))

# Calculating the volume
volume = calculate_cone_volume(radius, height)

# Displaying the result
print("The volume of the cone is:", volume)
