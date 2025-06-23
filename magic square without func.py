# Prompt the user to enter the order of the magic square (must be odd)
n = int(input("Enter the order of the magic square (must be odd): "))

# Check if the order is odd
if n % 2 == 0:
    print("The order must be an odd number.")
else:
    # Initialize an n x n matrix with zeros
    magic_square = [[0] * n for _ in range(n)]

    # Initialize the position for 1
    i, j = 0, n // 2

    # Fill the magic square
    for num in range(1, n * n + 1):
        magic_square[i][j] = num
        new_i, new_j = (i - 1) % n, (j + 1) % n
        if magic_square[new_i][new_j]:
            i += 1
        else:
            i, j = new_i, new_j

    # Print the magic square
    for row in magic_square:
        print(" ".join(str(x) for x in row))
