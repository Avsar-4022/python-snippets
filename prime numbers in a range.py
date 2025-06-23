def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_primes_in_range(start, end):
    prime_numbers = [num for num in range(start, end + 1) if is_prime(num)]
    if prime_numbers:
        print(f"The prime numbers between {start} and {end} are: {prime_numbers}")
    else:
        print(f"There are no prime numbers in the range {start} to {end}.")

# Example usage:
starting_range = int(input("Enter the starting number: "))
ending_range = int(input("Enter the ending number: "))
print_primes_in_range(starting_range, ending_range)
