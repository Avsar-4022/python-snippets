def get_last_n_digits(num, n):
    # Ensure n is a positive integer
    if not isinstance(n, int) or n <= 0:
        print("Please provide a positive integer value for 'n'.")
        return None

    # Calculate the last n digits
    last_n = abs(num) % (10 ** n)
    return last_n


# Example usage:
number = int(input("Enter a number: "))
n = int(input("Enter the value of 'n': "))
result = get_last_n_digits(number, n)

if result is not None:
    print(f"The last {n} digits of {number} are {result}")
