def calculate_triangle_area(s1, s2, s3):
    # Calculate the semi-perimeter
    s = (s1 + s2 + s3) / 2
    # Calculate the area using Heron's formula
    area = (s * (s - s1) * (s - s2) * (s - s3)) ** 0.5
    return area


def calculate_rectangle_area(length, breadth):
    return length * breadth


def calculate_circle_area(radius):
    import math
    return math.pi * radius ** 2


def main():
    while True:
        print("Select a polygon:")
        print("1. Triangle")
        print("2. Rectangle")
        print("3. Circle")
        choice = int(input("Enter your choice (1/2/3): "))

        if choice == 1:
            s1 = float(input("Enter the first side of the triangle: "))
            s2 = float(input("Enter the second side of the triangle: "))
            s3 = float(input("Enter the third side of the triangle: "))
            area = calculate_triangle_area(s1, s2, s3)
        elif choice == 2:
            length = float(input("Enter the length of the rectangle: "))
            breadth = float(input("Enter the breadth of the rectangle: "))
            area = calculate_rectangle_area(length, breadth)
        elif choice == 3:
            radius = float(input("Enter the radius of the circle: "))
            area = calculate_circle_area(radius)
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
            continue

        print(f"The area is: {area:.2f}")

        # Calculate perimeter (common for all polygons)
        if choice == 1:
            perimeter = s1 + s2 + s3
        elif choice == 2:
            perimeter = 2 * (length + breadth)
        else:
            perimeter = 2 * math.pi * radius

        print(f"The perimeter is: {perimeter:.2f}")

        repeat = input("Do you want to continue? (yes/no): ")
        if repeat.lower() != "yes":
            break


if __name__ == "__main__":
    main()
