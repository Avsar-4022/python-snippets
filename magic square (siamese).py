# Function to generate a magic square
def generate_magic_square(n):
    if n % 2 == 0:
        raise ValueError("Magic square is only possible for odd numbers.")

    magic_square = [[0] * n for _ in range(n)]

    num = 1
    i, j = 0, n // 2

    while num <= n * n:
        magic_square[i][j] = num
        num += 1
        new_i, new_j = (i - 1) % n, (j + 1) % n

        if magic_square[new_i][new_j]:
            i += 1
        else:
            i, j = new_i, new_j

    return magic_square


# Prompt the user to input an odd number
n = int(input("Enter an odd number for the magic square: "))

# Generate and display the magic square
try:
    magic_square = generate_magic_square(n)
    print(f"Magic Square for n = {n}:")
    for row in magic_square:
        print(" ".join(f"{num:2d}" for num in row))
except ValueError as e:
    print(e)
