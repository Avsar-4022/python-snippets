# Function to insert '1' before the decimal point
def insert_one_before_decimal(number):
    num_str = str(number)
    if '.' in num_str:
        integer_part, decimal_part = num_str.split('.')
        new_number = integer_part + '1.' + decimal_part
    else:
        new_number = num_str + '1'

    return new_number


# Taking input from the user
number = input("Enter a number: ")

# Inserting '1' before the decimal point and displaying the result
result = insert_one_before_decimal(number)
print("The number after inserting '1' before the decimal point is:", result)
