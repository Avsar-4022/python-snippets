# without using third variable
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
a = a + b
b = a - b
a = a - b
print(f"After swapping the value of the first number is {a} and that of the second number is {b} ")
