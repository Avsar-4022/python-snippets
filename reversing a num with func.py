
def reverse_number(number):
    reversed_num = 0
    while number > 0:
        digit = number % 10
        reversed_num = reversed_num * 10 + digit
        number //= 10
    return reversed_num



num = int(input("Enter a number: "))


print(f"The reversed number is {reverse_number(num)}.")
