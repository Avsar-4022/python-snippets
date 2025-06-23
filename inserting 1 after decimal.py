# Function to insert '1' as the first digit after the decimal point
def insert_one_after_decimal(number):
    num_str = str(number)
    if '.' in num_str:
        integer_part, decimal_part = num_str.split('.')
        new_decimal_part = '1' + decimal_part
        new_number = integer_part + '.' + new_decimal_part
    else:
        new_number = num_str + '.1'

    return new_number


# Taking input from the user
number = input("Enter a number: ")

# Inserting '1' after the decimal point and displaying the result
result = insert_one_after_decimal(number)
print("The number after inserting '1' after the decimal point is:", result)
