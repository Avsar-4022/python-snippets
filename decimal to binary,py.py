# Function to convert decimal to binary manually
def decimal_to_binary_manual(n):
    binary_num = ""
    while n > 0:
        binary_num = str(n % 2) + binary_num
        n = n // 2
    return binary_num


# Prompt the user to input a decimal number
num = int(input("Enter a decimal number: "))

# Convert and display the binary number
print(f"The binary representation of {num} is {decimal_to_binary_manual(num)}.")
