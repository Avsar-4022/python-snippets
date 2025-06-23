import math

a = int(input("Enter the first side of the triangle: "))
b = int(input("Enter the second side of the triangle: "))
c = int(input("Enter the third side of the triangle: "))
s = (a + b + c) / 2

area = float(math.sqrt((s * (s - a) * (s - b) * (s - c))))
print("Area of the triangle is %.2f", area)
