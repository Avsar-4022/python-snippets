def swap_last_two_digits(num):
    num_str = str(num)
    num_list = list(num_str)

    # Swap the last two digits
    num_list[-1], num_list[-2] = num_list [-2], num_list[-1]

    # Join the list elements and convert back to an integer
    swapped_num = int("".join(num_list))
    return swapped_num


# Example usage:
number = int(input("Enter a number: "))
swapped_number = swap_last_two_digits(number)
print(f"The number with swapped last two digits: {swapped_number}")
